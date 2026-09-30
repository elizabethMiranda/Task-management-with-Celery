# state-machine — Órdenes de Compra

Sistema de órdenes de compra con **máquina de estados** y **arquitectura hexagonal**. Guarda las órdenes en **PostgreSQL** (Django ORM) y verifica el producto contra **FakeStoreAPI** de forma asíncrona con **Celery + Redis**.

**Stack:** Python 3.14 · Django 5 · PostgreSQL · Celery 5 · Redis · `psycopg[binary]` · `requests`

## Estructura

```
domain/           Entidad PurchaseOrder, estados, transiciones, excepciones (sin dependencias externas)
application/      Casos de uso y ports (port/input, port/output)
infrastructure/   Django (config, modelos), DjangoRepository, Celery (app, tasks, dispatcher)
test_manual.py    Prueba del dominio
test_full_flow.py Prueba del flujo completo
```

## Estados

```
CREADA → APROBADA → PAGADA → ENVIADA → ENTREGADA → FINALIZADA
```
`CANCELADA` se permite desde cualquier estado excepto `ENTREGADA` y `FINALIZADA`. Cualquier otra transición lanza `InvalidTransitionError`.

## Instalación

Desde la raíz del proyecto:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

createdb purchase_order_db
python manage.py migrate
```

Ajusta las credenciales de PostgreSQL en `infrastructure/config/settings.py` si es necesario.

## Prueba 1 — Dominio

No necesita base de datos ni Redis.

```bash
python test_manual.py
```

Recorre el ciclo completo de la orden. La última línea debe mostrar el error esperado al intentar reabrir una orden finalizada.

## Prueba 2 — Flujo completo

Usa una terminal para cada comando:

```bash
brew services start postgresql@16                                  # 1. PostgreSQL
redis-server                                                       # 2. Redis
celery -A infrastructure.celery.celery_app worker --loglevel=info  # 3. Worker
python test_full_flow.py                                           # 4. Script
```

El script imprime `Orden creada y tarea despachada correctamente`. Unos segundos después, el worker muestra la consulta a FakeStoreAPI y termina con `succeeded`.

Para verificar que se guardó:
```bash
psql purchase_order_db -c "SELECT * FROM purchase_orders;"
```

## Problemas comunes

- **`ModuleNotFoundError`**: ejecuta los comandos desde la raíz del proyecto.
- **`unregistered task`**: en `celery_app.py` usa `app.autodiscover_tasks(["infrastructure.celery"])` y reinicia el worker.
- **`Connection refused` (puerto 6379)**: Redis no está corriendo.

"""Tareas asíncronas de Celery."""

import requests

from infrastructure.celery.celery_app import app


@app.task
def verificar_producto_externo(order_id: str, producto_id: int) -> dict:
    print(f"Consultando producto {producto_id} para la orden {order_id}...")

    response = requests.get(f"https://fakestoreapi.com/products/{producto_id}")
    datos_producto = response.json()

    print(f"Producto verificado para la orden {order_id}: {datos_producto}")

    return datos_producto

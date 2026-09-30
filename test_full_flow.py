import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "infrastructure.config.settings")
django.setup()

from decimal import Decimal

from domain.entities.purchase_order import PurchaseOrder
from application.port.input.create_purchase_order_usecase import (
    CreatePurchaseOrderUseCase,
)
from infrastructure.persistence.django_repository import DjangoRepository
from infrastructure.celery.celery_task_dispatcher import CeleryTaskDispatcher

repository = DjangoRepository()
task_dispatcher = CeleryTaskDispatcher()

usecase = CreatePurchaseOrderUseCase(repository, task_dispatcher)

orden = PurchaseOrder(
    order_id="OC-202",
    producto="Teclado Mecánico",
    cantidad=3,
    costo_unitario=Decimal("1200.00"),
)

usecase.ejecutar(orden, producto_id=3)

print("Orden creada y tarea despachada correctamente")

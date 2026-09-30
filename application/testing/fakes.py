"""Adapters falsos, solo para pruebas manuales sin infraestructura real."""

from domain.entities.purchase_order import PurchaseOrder
from application.port.output.repository_port import RepositoryPort
from application.port.output.task_dispatcher_port import TaskDispatcherPort
from application.port.output.product_catalog_port import ProductCatalogPort


class FakeRepository(RepositoryPort):

    def __init__(self):
        self._ordenes = {}

    def guardar(self, orden: PurchaseOrder) -> None:
        self._ordenes[orden.order_id] = orden
        print(f"[FAKE REPOSITORY] Orden {orden.order_id} guardada en memoria")

    def obtener_por_id(self, order_id: str) -> PurchaseOrder:
        return self._ordenes[order_id]


class FakeTaskDispatcher(TaskDispatcherPort):

    def despachar_verificacion_producto(self, order_id: str, producto_id: int) -> None:
        print(f"[FAKE CELERY] Se despachó la verificación del producto {producto_id} para la orden {order_id}")


class FakeProductCatalog(ProductCatalogPort):

    def obtener_producto(self, producto_id: int) -> dict:
        print(f"[FAKE CATALOG] Consultando producto {producto_id} (simulado)")
        return {"id": producto_id, "title": "Producto simulado", "price": 99.99}
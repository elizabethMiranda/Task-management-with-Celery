"""Adapter real del repositorio, usando el ORM de Django."""

from decimal import Decimal

from application.port.output.repository_port import RepositoryPort
from domain.entities.enum.states import PurchaseOrderState
from domain.entities.purchase_order import PurchaseOrder
from infrastructure.purchase_order_app.models import PurchaseOrderModel


class DjangoRepository(RepositoryPort):

    def guardar(self, orden: PurchaseOrder) -> None:
        PurchaseOrderModel.objects.update_or_create(
            order_id=orden.order_id,
            defaults={
                "producto": orden.producto,
                "cantidad": orden.cantidad,
                "costo_unitario": orden.costo_unitario,
                "costo_total": orden.costo_total,
                "estado": orden.estado.value,
            },
        )

    def obtener_por_id(self, order_id: str) -> PurchaseOrder:
        modelo = PurchaseOrderModel.objects.get(order_id=order_id)

        return PurchaseOrder(
            order_id=modelo.order_id,
            producto=modelo.producto,
            cantidad=modelo.cantidad,
            costo_unitario=Decimal(modelo.costo_unitario),
            estado=PurchaseOrderState(modelo.estado),
        )

from abc import ABC, abstractmethod
from domain.entities.purchase_order import PurchaseOrder

"""Contrato del caso de uso: crear una orden de compra."""
class CreatePurchaseOrderPort(ABC):
    @abstractmethod
    def ejecutar(self, orden: PurchaseOrder, producto_id: int) -> None:
        pass
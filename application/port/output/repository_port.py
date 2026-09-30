"""Contrato para guardar y leer órdenes de compra."""

from abc import ABC, abstractmethod

from domain.entities.purchase_order import PurchaseOrder


class RepositoryPort(ABC):
    @abstractmethod
    def guardar(self, orden: PurchaseOrder) -> None:
        pass

    @abstractmethod
    def obtener_por_id(self, order_id: str) -> PurchaseOrder:
        pass

from abc import ABC, abstractmethod

"""Contrato para consultar el catálogo externo de productos."""
class ProductCatalogPort(ABC):
    @abstractmethod
    def obtener_producto(self, producto_id: int) -> dict:
        pass

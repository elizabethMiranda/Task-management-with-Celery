from abc import ABC, abstractmethod

"""Contrato para despachar tareas asíncronas."""
class TaskDispatcherPort(ABC):
    @abstractmethod
    def despachar_verificacion_producto(self, order_id: str, producto_id: int) -> None:
        pass
"""Entidad de dominio: Orden de Compra."""

from decimal import Decimal

from domain.entities.enum.states import PurchaseOrderState
from domain.services.transitions import TransitionTable
from domain.exceptions.domain_exceptions import InvalidTransitionError


class PurchaseOrder:

    def __init__(
        self,
        order_id: str,
        producto: str,
        cantidad: int,
        costo_unitario: Decimal,
        estado: PurchaseOrderState = PurchaseOrderState.CREADA,
    ):
        self.order_id = order_id
        self.producto = producto
        self.cantidad = cantidad
        self.costo_unitario = costo_unitario
        self.costo_total = cantidad * costo_unitario
        self._estado = estado

    @property
    def estado(self) -> PurchaseOrderState:
        return self._estado

    def cambiar_estado(self, nuevo_estado: PurchaseOrderState, transition_table: TransitionTable) -> None:
        es_valida = transition_table.is_allowed(self._estado, nuevo_estado)
        if es_valida:
            tiene_costo_valida = self.costo_total > 0
            tiene_producto_valido = self.producto.strip() != ""

            if tiene_costo_valida and tiene_producto_valido:
                self._estado = nuevo_estado
            elif tiene_costo_valida == False:
                raise ValueError("El costo total debe ser mayor a cero")
            else:
                raise ValueError("El producto no puede estar vacío")
        else:    
            raise InvalidTransitionError(self._estado, nuevo_estado)
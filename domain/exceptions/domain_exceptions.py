"""Excepciones propias del dominio de la orden de compra."""

from domain.entities.enum.states import PurchaseOrderState


class InvalidTransitionError(Exception):

    def __init__(self, from_state: PurchaseOrderState, to_state: PurchaseOrderState):
        self.from_state = from_state
        self.to_state = to_state
        super().__init__(
            f"No se puede pasar de '{from_state.value}' a '{to_state.value}'"
        )
"""Tabla de transiciones válidas para la orden de compra."""


from domain.entities.enum.states import PurchaseOrderState

class TransitionTable:
    def __init__(self):
        self._transitions: dict[PurchaseOrderState, set[PurchaseOrderState]] = {}

    def allow(
        self,
        from_state: PurchaseOrderState,
        to_state: PurchaseOrderState,
    ) -> "TransitionTable":
        self._transitions.setdefault(from_state, set()).add(to_state)
        return self

    def is_allowed(
        self,
        from_state: PurchaseOrderState,
        to_state: PurchaseOrderState,
    ) -> bool:
        return to_state in self._transitions.get(from_state, set())

def build_purchase_order_transitions() -> "TransitionTable":
    return (
            TransitionTable()
            .allow(PurchaseOrderState.CREADA, PurchaseOrderState.APROBADA)
            .allow(PurchaseOrderState.CREADA, PurchaseOrderState.CANCELADA)
            .allow(PurchaseOrderState.APROBADA, PurchaseOrderState.PAGADA)
            .allow(PurchaseOrderState.APROBADA, PurchaseOrderState.CANCELADA)
            .allow(PurchaseOrderState.PAGADA, PurchaseOrderState.ENVIADA)
            .allow(PurchaseOrderState.PAGADA, PurchaseOrderState.CANCELADA)
            .allow(PurchaseOrderState.ENVIADA, PurchaseOrderState.ENTREGADA)
            .allow(PurchaseOrderState.ENVIADA, PurchaseOrderState.CANCELADA)
            .allow(PurchaseOrderState.ENTREGADA, PurchaseOrderState.FINALIZADA) 
    )
from decimal import Decimal
from domain.entities.enum.states import PurchaseOrderState
from domain.entities.purchase_order import PurchaseOrder
from domain.services.transitions import build_purchase_order_transitions
from domain.exceptions.domain_exceptions import InvalidTransitionError

tabla = build_purchase_order_transitions()

orden = PurchaseOrder(
    order_id="OC-001",
    producto="Laptop Dell",
    cantidad=3,
    costo_unitario=Decimal("15000.00"),
)

print("Estado inicial:", orden.estado)
print("Costo total:", orden.costo_total)

orden.cambiar_estado(PurchaseOrderState.APROBADA, tabla)
print("Después de aprobar:", orden.estado)

orden.cambiar_estado(PurchaseOrderState.PAGADA, tabla)
print("Después de pagar:", orden.estado)

orden.cambiar_estado(PurchaseOrderState.ENVIADA, tabla)
print("Después de enviar:", orden.estado)

orden.cambiar_estado(PurchaseOrderState.ENTREGADA, tabla)
print("Después de entregar:", orden.estado)

orden.cambiar_estado(PurchaseOrderState.FINALIZADA, tabla)
print("Después de finalizar:", orden.estado)

try:
    orden.cambiar_estado(PurchaseOrderState.APROBADA, tabla)
except InvalidTransitionError as error:
    print("Error esperado (no se puede reabrir una orden finalizada):", error)

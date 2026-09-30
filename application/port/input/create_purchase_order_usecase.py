from domain.entities.purchase_order import PurchaseOrder
from application.port.input.create_purchase_order_port import CreatePurchaseOrderPort
from application.port.output.repository_port import RepositoryPort
from application.port.output.task_dispatcher_port import TaskDispatcherPort

"""Caso de uso: crear una orden de compra."""
class CreatePurchaseOrderUseCase(CreatePurchaseOrderPort):
    def __init__(self, repository: RepositoryPort, task_dispatcher: TaskDispatcherPort):
        self._repository = repository
        self._task_dispatcher = task_dispatcher

    def ejecutar(self, orden: PurchaseOrder, producto_id: int) -> None:
        self._repository.guardar(orden)
        self._task_dispatcher.despachar_verificacion_producto(orden.order_id, producto_id)
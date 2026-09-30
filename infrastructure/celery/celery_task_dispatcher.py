"""Adapter real que despacha tareas usando Celery."""

from application.port.output.task_dispatcher_port import TaskDispatcherPort
from infrastructure.celery.tasks import verificar_producto_externo


class CeleryTaskDispatcher(TaskDispatcherPort):

    def despachar_verificacion_producto(self, order_id: str, producto_id: int) -> None:
        verificar_producto_externo.delay(order_id, producto_id)

"""Definición de los estados posibles de una Orden de Compra."""

from enum import Enum


class PurchaseOrderState(Enum):
    CREADA = "creada"
    APROBADA = "aprobada"
    PAGADA = "pagada"
    ENVIADA = "enviada"
    ENTREGADA = "entregada"
    FINALIZADA = "finalizada"
    CANCELADA = "cancelada"

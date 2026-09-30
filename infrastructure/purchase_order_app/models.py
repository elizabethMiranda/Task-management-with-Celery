"""Modelo Django: representación en base de datos de una orden de compra."""

from django.db import models


class PurchaseOrderModel(models.Model):
    order_id = models.CharField(max_length=50, unique=True, primary_key=True)
    producto = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    costo_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    costo_total = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.CharField(max_length=20)

    class Meta:
        db_table = "purchase_orders"

    def __str__(self):
        return f"{self.order_id} - {self.estado}"
# Create your models here.

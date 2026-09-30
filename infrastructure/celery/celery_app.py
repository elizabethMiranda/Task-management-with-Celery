"""Configuración de Celery, conectada a Django."""

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "infrastructure.config.settings")

app = Celery("purchase_order_service")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(["infrastructure.celery"])

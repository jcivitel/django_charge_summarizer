import os

from django.apps import AppConfig
from django.conf import settings


class BackendConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_crg_backend"

    def ready(self):
        media_path = os.path.join(settings.MEDIA_ROOT, "upload")
        os.makedirs(media_path, exist_ok=True)
        media_path = os.path.join(settings.MEDIA_ROOT, "processed")
        os.makedirs(media_path, exist_ok=True)

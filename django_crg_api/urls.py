from django.urls import path, include
from rest_framework import routers

from django_crg_api.views import ChargeInvoiceViewSet

router = routers.DefaultRouter()
router.register(r"charge-invoice", ChargeInvoiceViewSet, "charge-invoice")
urlpatterns = [
    path("v1/", include(router.urls)),
]

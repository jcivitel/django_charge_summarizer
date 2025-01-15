from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from django_crg_api.serializers import ChargeInvoiceSerializer, ChargeInvoiceFilter
from django_crg_backend.models import ChargeInvoice


class ChargeInvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ChargeInvoice.objects.all()
    serializer_class = ChargeInvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ChargeInvoiceFilter
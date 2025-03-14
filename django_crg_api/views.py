from django.db.models import Sum
from django.db.models.functions import TruncDate
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, serializers

from django_crg_api.serializers import ChargeInvoiceSerializer, ChargeInvoiceFilter, ChargeTotalkWhSerializer, \
    ChargeTotalkWhPerCustomerSerializer
from django_crg_backend.models import ChargeInvoice, Customer


class ChargeInvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ChargeInvoice.objects.all()
    serializer_class = ChargeInvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ChargeInvoiceFilter


class ChargeTotalkWhViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ChargeInvoice.objects.all()
    serializer_class = ChargeTotalkWhSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ChargeInvoiceFilter

    def get_queryset(self):
        data = (
            ChargeInvoice.objects
            .annotate(date=TruncDate('charge_invoice_date'))  # Truncate timestamp to date
            .annotate(total_used_kwh=Sum('total_kwh'))
            .values('charge_invoice_date', 'total_kwh', 'charge_customer')
            .order_by('date')  # Optional: Order by date
        )
        return data
class TotalKwhPerCustomerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ChargeTotalkWhPerCustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ChargeInvoiceFilter

    def get_queryset(self):
        data = (
            ChargeInvoice.objects
            .values('charge_customer')
            .annotate(total_kwh=Sum('total_kwh'))
        )
        return data
from django.db.models import Sum
from django.db.models.functions import TruncDate
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from django_crg_api.serializers import ChargeInvoiceSerializer, ChargeInvoiceFilter, ChargeTotalkWhSerializer
from django_crg_backend.models import ChargeInvoice


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
            .values('charge_invoice_date', "charge_customer")  # Group by date
            .annotate(total_kwh=Sum('total_kwh'))  # Sum total_kwh for each day
            .order_by('date')  # Optional: Order by date
        )
        return data

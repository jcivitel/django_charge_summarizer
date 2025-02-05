from django_filters import rest_framework as filters
from rest_framework import serializers

from django_crg_backend.models import ChargeInvoice, Customer


class ChargeInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeInvoice
        fields = '__all__'


class ChargeInvoiceFilter(filters.FilterSet):
    invoice_month = filters.NumberFilter(field_name="charge_invoice_date", lookup_expr="month")
    invoice_year = filters.NumberFilter(field_name="charge_invoice_date", lookup_expr="year")
    invoice_customer = filters.ModelChoiceFilter(queryset=Customer.objects.all(), field_name="charge_customer")

    class Meta:
        model = ChargeInvoice
        fields = ['invoice_month', 'invoice_year', 'invoice_customer']


class ChargeTotalkWhSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeInvoice
        fields = ['charge_invoice_date', 'total_kwh', 'charge_customer.id']

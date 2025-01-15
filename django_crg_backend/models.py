from django.db import models


class Customer(models.Model):
    customer_no = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100, null=True)
    customer_address = models.TextField(null=True)
    customer_email = models.EmailField(null=True)
    vat_id = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.customer_no


class ChargingStation(models.Model):
    station_name = models.CharField(max_length=100)
    station_address = models.TextField(null=True)
    station_capacity = models.TextField(null=True)

    def __str__(self):
        return self.station_name


class ChargeInvoice(models.Model):
    charge_invoice_no = models.CharField(max_length=50)
    charge_invoice_date = models.DateField()
    charge_reference_no = models.CharField(max_length=100)
    charge_station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)
    charge_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price_per_kwh = models.FloatField()
    total_kwh = models.FloatField()
    total_amount = models.FloatField()
    tax_amount = models.FloatField()

    def __str__(self):
        return self.charge_invoice_no

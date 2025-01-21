import os
import re
import shutil
import zipfile
from datetime import datetime

from PyPDF2 import PdfReader
from celery import shared_task
from django.conf import settings

from django_crg_backend.models import ChargeInvoice, Customer, ChargingStation


@shared_task
def process_invoice(filepath):
    upload_path = os.path.join(settings.MEDIA_ROOT, 'upload')
    if os.path.commonpath([filepath, upload_path]) == upload_path:
        print(f'Processing file: {filepath}')
        with open(filepath, 'rb') as f:
            reader = PdfReader(f)
            num_pages = len(reader.pages)
            text = ''
            for page_num in range(num_pages):
                text += reader.pages[page_num].extract_text()

        invoice_no = re.search(r'Rechnungsnummer (\w+)', text).group(1)
        invoice_date = re.search(r'Rechnungsdatum (.+)', text).group(1)
        invoice_reference = re.search(r'Referenznummer(\S+)', text).group(1)
        invoice_charging_station = re.search(r'Ladestation(\n)(\w+)', text).group(2)
        invoice_customer = re.search(r'Kundennummer (\w+)', text).group(1)
        price_per_kwh = re.search(r'Energy fee (\S+)', text).group(1)
        try:
            invoice_total_kwh = re.search(r'(\d+\.\d+)\s*/\s*kWh\s*(\d+\.\d+)\s*kWh', text).group(2)
        except AttributeError:
            invoice_total_kwh = re.search(r'(\d+\.\d+)\s*/\s*kWh\s*(\d+)\s*kWh', text).group(2)
        invoice_tax_amount = re.search(r'Gesamtsumme Steuern (\S+)', text).group(1)
        invoice_total_amount = re.search(r'Gesamtbetrag \(EUR\) (\S+)', text).group(1)
        # --------------------------------
        cus_id, created = Customer.objects.get_or_create(customer_no=invoice_customer)
        charge_id, created = ChargingStation.objects.get_or_create(station_name=invoice_charging_station)
        ChargeInvoice.objects.get_or_create(
            charge_invoice_no=invoice_no,
            charge_invoice_date=datetime.strptime(invoice_date, "%Y/%m/%d"),
            charge_reference_no=invoice_reference,
            charge_station=charge_id,
            charge_customer=cus_id,
            price_per_kwh=price_per_kwh,
            total_kwh=invoice_total_kwh,
            total_amount=invoice_total_amount,
            tax_amount=invoice_tax_amount
        )
        try:
            os.rename(filepath, os.path.join(settings.MEDIA_ROOT, 'processed', os.path.basename(filepath)))
        except FileExistsError:
            os.remove(filepath)
    else:
        raise FileNotFoundError('File not found in the upload folder')


@shared_task
def unpack_zip(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(os.path.join(settings.MEDIA_ROOT, 'upload'))
    os.remove(zip_file)
    root_dir = os.path.join(settings.MEDIA_ROOT, 'upload')
    for folder_name in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder_name)
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                new_path = os.path.join(root_dir, file_name)
                shutil.move(file_path, new_path)
            os.rmdir(folder_path)


@shared_task
def check_upload_folder():
    upload_folder = os.path.join(settings.MEDIA_ROOT, 'upload')
    if len(os.listdir(upload_folder)) == 0:
        print('No files found in the upload folder')
        return 0
    for filename in os.listdir(upload_folder):
        filepath = os.path.join(upload_folder, filename)
        if filename.endswith('.pdf'):
            process_invoice.delay(filepath)
        elif filename.endswith('.zip'):
            unpack_zip.delay(filepath)

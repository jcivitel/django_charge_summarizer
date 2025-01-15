import os

from django.conf import settings
from django.core.management.base import BaseCommand

from django_crg_backend.tasks import process_invoice, unpack_zip


class Command(BaseCommand):
    help = 'Process all PDF files in the media/upload folder and save the processed data in the models'

    def handle(self, *args, **kwargs):
        upload_folder = os.path.join(settings.MEDIA_ROOT, 'upload')
        if len(os.listdir(upload_folder)) == 0:
            print('No files found in the upload folder')
            return 0
        for filename in os.listdir(upload_folder):
            if filename.endswith('.pdf'):
                process_invoice(os.path.join(upload_folder, filename))
            if filename.endswith('.zip'):
                unpack_zip(os.path.join(upload_folder, filename))

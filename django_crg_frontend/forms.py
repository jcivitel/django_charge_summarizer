from django import forms
from django.utils.translation import gettext_lazy as _


class UploadFileForm(forms.Form):
    files = forms.FileField(
        label=_('Select a file'),
        help_text=_('Only .zip or .pdf files are allowed'),
        widget=forms.ClearableFileInput(
            attrs={
                'accept': '.zip,.pdf',
                'class': 'form-control',
                'multiple': '',
            }
        )
    )

from django import forms
from .models import MultipleFiles

class MultipleFileForms(forms.ModelForm):
    class Meta:
        model = MultipleFiles
        fields = ('csv_file', 'zip_file')
from django import forms
from .models import CsvFile, ImageZipFile, MultipleFiles

class CsvFileModelForm(forms.ModelForm):
    class Meta:
        model = CsvFile
        fields = ('file_name',)

class ImageZipFileForm(forms.ModelForm):
    class Meta:
        model = ImageZipFile
        fields = ('file_name',)

class MultipleFileForms(forms.ModelForm):
    class Meta:
        model = MultipleFiles
        fields = ('csv_file', 'zip_file')
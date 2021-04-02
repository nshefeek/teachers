from django.forms import ModelForm
from .models import CsvFile, ImageZipFile

class CsvFileModelForm(ModelForm):
    class Meta:
        model = CsvFile
        fields = ('file_name',)

class ImageZipFileForm(ModelForm):
    class Meta:
        model = ImageZipFile
        fields = ('file_name',)
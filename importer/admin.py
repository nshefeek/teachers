from django.contrib import admin
from .models import CsvFile, ImageZipFile, MultipleFiles

# Register your models here.
admin.site.register([CsvFile, ImageZipFile, MultipleFiles])
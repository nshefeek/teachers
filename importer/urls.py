from django.urls import path
from .views import import_csv_view

app_name = 'importer'

urlpatterns = [
    path('', import_csv_view, name='import-files'),
]
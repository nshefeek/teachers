from django.urls import path
from .views import import_file_view

app_name = 'importer'

urlpatterns = [
    path('', import_file_view, name='import-files'),
]
from django.urls import path
from .views import TeacherListView, import_csv_view

urlpatterns = [
    path('', TeacherListView.as_view(), name='index'),
    path('import/', import_csv_view, name='import'),
]
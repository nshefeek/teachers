from django.urls import path
from .views import TeacherListView, TeacherDetailView, SearchResultsView

app_name = 'directory'

urlpatterns = [
    path('', TeacherListView.as_view(), name='listing'),
    path('<int:id>/', TeacherDetailView.as_view(), name='detail'),
    path('search/', SearchResultsView.as_view(), name='search')
]
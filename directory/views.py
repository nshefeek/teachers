from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Teacher

# Create your views here.
class TeacherListView(ListView):
    model = Teacher

class TeacherDetailView(DetailView):
    pass

def import_csv_view(request):
    return render(request, 'import.html')
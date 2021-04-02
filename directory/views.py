from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Teacher

# Create your views here.
class TeacherListView(ListView):
    model = Teacher

class TeacherDetailView(DetailView):
    model = Teacher
    
    def get_object(self):
        print(self.request)
        id_ = self.kwargs.get("id")
        return get_object_or_404(Teacher, id=id_)
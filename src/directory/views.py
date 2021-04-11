from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .forms import SearchForm
from .models import Teacher

# Create your views here.
class TeacherListView(ListView):
    model = Teacher
    form_class = SearchForm
    

class TeacherDetailView(DetailView):
    model = Teacher
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Teacher, id=id_)


class SearchResultsView(ListView):
    model = Teacher
    template_name = 'search_results.html'

    def get_queryset(self):
        q = self.request.GET['q']
        choice = self.request.GET['choice']
        if choice == 'subject':
            return Teacher.objects.filter(subjects__title__istartswith=q)
        return Teacher.objects.filter(last_name__istartswith=q)
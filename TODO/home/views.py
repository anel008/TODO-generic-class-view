from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,ListView,View
from .models import Todo
# Create your views here.

class create_note(CreateView):
    model = Todo
    template_name = 'add.html'
    fields = ('title','body')
    success_url = '/home'

class list_note(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'note'

class view_note(DetailView):
    model = Todo
    template_name = 'notes.html'
    context_object_name = 'note'
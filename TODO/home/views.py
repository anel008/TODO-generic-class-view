from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,ListView,View
from .models import Todo
from .form import NoteForm
from django.urls import reverse_lazy
# Create your views here.

class CreateNote(CreateView):
    model = Todo
    template_name = 'add.html'
    fields = ('title','body')
    success_url = '/'

class ListNote(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'note'

class ViewNote(DetailView):
    model = Todo
    template_name = 'notes.html'
    context_object_name = 'note'

class DeleteNote(DeleteView):
    model = Todo
    template_name ='delete.html'
    success_url = reverse_lazy('/')

class UpdateNote(UpdateView):
    model = Todo
    template_name = 'update.html'
    fields = ('title','body')
    success_url=reverse_lazy('/')
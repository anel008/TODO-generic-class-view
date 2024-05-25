from django import forms
from .models import Todo

class NoteForm(forms.ModelForm):
    model = Todo
    files = ['title','body']
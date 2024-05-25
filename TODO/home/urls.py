from django.urls import path
from .views import create_note,list_note,view_note


urlpatterns = [
    path('add',create_note.as_view(), name='add'),
    path('',list_note.as_view(),name=''),
    path('viewnote/<int:id>',view_note.as_view(),name='viewnote')
]

from django.urls import path
from .views import CreateNote,ListNote,ViewNote,DeleteNote


urlpatterns = [
    path('add',CreateNote.as_view(), name='add'),
    path('',ListNote.as_view(),name=''),
    path('viewnote/<int:pk>',ViewNote.as_view(),name='viewnote'),
    path('deletenote/<int:pk>',DeleteNote.as_view(),name='delete')
]

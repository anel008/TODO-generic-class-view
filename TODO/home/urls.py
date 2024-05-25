from django.urls import path
from .views import CreateNote,ListNote,ViewNote,DeleteNote,UpdateNote


urlpatterns = [
    path('add',CreateNote.as_view(), name='add'),
    path('',ListNote.as_view(),name=''),
    path('viewnote/<int:pk>',ViewNote.as_view(),name='viewnote'),
    path('delete/<int:pk>',DeleteNote.as_view(),name='delete'),
    path('update/<int:pk>',UpdateNote.as_view(),name='update')
]

from django.urls import path
from .views import create_note_view, list_notes_view

urlpatterns = [
    path("create/", create_note_view),
     path("", list_notes_view),
]
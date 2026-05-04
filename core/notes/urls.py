from django.urls import path
from .views import create_note_view

urlpatterns = [
    path("create/", create_note_view),
]
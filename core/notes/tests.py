from django.test import TestCase
from notes.services.note_service import create_note
from django.contrib.auth.models import User

user = User.objects.first()

note = create_note(user=user, data={
    "title": "Shell Test",
    "content": "Testing service layer"
})

print(note)
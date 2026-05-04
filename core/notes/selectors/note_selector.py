from notes.models import Note

def get_notes_by_user(user):
    return Note.objects.filter(user=user)
from notes.models import Note

def create_note(user, data):
    return Note.objects.create(
        user=user,
        title=data.get("title"),
        content=data.get("content")
    )
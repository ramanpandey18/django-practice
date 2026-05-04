from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import get_user_model
import json

from notes.services.note_service import create_note
from notes.selectors.note_selector import get_notes_by_user

User = get_user_model()

@csrf_exempt
def create_note_view(request):
    if request.method == "POST":
        data = json.loads(request.body)

        user = User.objects.first()

        note = create_note(user=user, data=data)

        return JsonResponse({"id": note.id})
    

def list_notes_view_v1(request):
    user = User.objects.first()

    notes = get_notes_by_user(user)

    data = [
        {
            "id": n.id,
            "title": n.title,
            "content": n.content
        }
        for n in notes
    ]

    return JsonResponse(data, safe=False)

def to_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None
    
def list_notes_view(request):
    user = User.objects.first()

    sort_by = request.GET.get("sort")
    search = request.GET.get("search")
    limit = to_int(request.GET.get("limit"))
    offset = to_int(request.GET.get("offset"))

    notes = get_notes_by_user(user, sort_by=sort_by, search=search, limit=limit, offset=offset)

    data = [
        {
            "id": n.id,
            "title": n.title,
            "content": n.content
        }
        for n in notes
    ]

    return JsonResponse(data, safe=False)
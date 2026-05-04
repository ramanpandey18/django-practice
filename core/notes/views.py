from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import get_user_model
import json

from notes.services.note_service import create_note

User = get_user_model()

@csrf_exempt
def create_note_view(request):
    if request.method == "POST":
        data = json.loads(request.body)

        user = User.objects.first()

        note = create_note(user=user, data=data)

        return JsonResponse({"id": note.id})
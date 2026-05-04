# from notes.models import Note

# def get_notes_by_user(user):
#     return Note.objects.filter(user=user)

from notes.models import Note
from notes.strategies.sort_strategy import get_sort_strategy
from django.db.models import Q


def get_notes_by_user(user, sort_by=None, search=None, limit=None, offset=None):
    queryset = Note.objects.filter(user=user)

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search)
        )
    
    if offset:
        queryset = queryset[offset:]

    if limit:
        queryset = queryset[:limit]
        
    strategy = get_sort_strategy(sort_by)
    return strategy.sort(queryset)
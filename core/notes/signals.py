from django.db.models.signals import post_save
from django.dispatch import receiver
from notes.models import Note


@receiver(post_save, sender=Note)
def note_created_handler(sender, instance, created, **kwargs):
    if created:
        print(f"✅ Note created: {instance.title}")
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from notes.models import Note

@receiver(pre_save, sender=Note)
def note_pre_save(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = Note.objects.get(pk=instance.pk)
    except Note.DoesNotExist:
        return

    if old_instance.image and old_instance.image != instance.image:
        old_instance.image.delete(save=False)

@receiver(post_delete, sender=Note)
def note_post_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from event.models import Event

@receiver(pre_save, sender=Event)
def event_pre_save(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = Event.objects.get(pk=instance.pk)
    except Event.DoesNotExist:
        return

    if old_instance.image and old_instance.image != instance.image:
        old_instance.image.delete(save=False)

@receiver(post_delete, sender=Event)
def event_post_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

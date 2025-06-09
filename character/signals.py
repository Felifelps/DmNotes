from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from character.models import Character

@receiver(pre_save, sender=Character)
def character_pre_save(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = Character.objects.get(pk=instance.pk)
    except Character.DoesNotExist:
        return

    if old_instance.image and old_instance.image != instance.image:
        old_instance.image.delete(save=False)

@receiver(post_delete, sender=Character)
def character_post_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

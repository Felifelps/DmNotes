from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from place.models import Place

@receiver(pre_save, sender=Place)
def place_pre_save(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = Place.objects.get(pk=instance.pk)
    except Place.DoesNotExist:
        return

    if old_instance.image and old_instance.image != instance.image:
        old_instance.image.delete(save=False)

@receiver(post_delete, sender=Place)
def place_post_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

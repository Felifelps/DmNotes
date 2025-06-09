from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from dungeon.models import Dungeon

@receiver(pre_save, sender=Dungeon)
def dungeon_pre_save(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = Dungeon.objects.get(pk=instance.pk)
    except Dungeon.DoesNotExist:
        return

    if old_instance.image and old_instance.image != instance.image:
        old_instance.image.delete(save=False)

@receiver(post_delete, sender=Dungeon)
def dungeon_post_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

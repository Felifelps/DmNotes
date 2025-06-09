from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from item.models import Item

@receiver(pre_save, sender=Item)
def item_pre_save(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = Item.objects.get(pk=instance.pk)
    except Item.DoesNotExist:
        return

    if old_instance.image and old_instance.image != instance.image:
        old_instance.image.delete(save=False)

@receiver(post_delete, sender=Item)
def item_post_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from sheet.models import Sheet

@receiver(pre_save, sender=Sheet)
def sheet_pre_save(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = Sheet.objects.get(pk=instance.pk)
    except Sheet.DoesNotExist:
        return

    if old_instance.image and old_instance.image != instance.image:
        old_instance.image.delete(save=False)

@receiver(post_delete, sender=Sheet)
def sheet_post_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

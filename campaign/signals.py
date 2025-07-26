from django.db.models.signals import post_save
from django.dispatch import receiver

from campaign.models import Campaign
from tags.models import Tag

@receiver(post_save, sender=Campaign)
def campaign_post_save(sender, instance, created, **kwargs):
    if created:
        for name in ["Personagens", "Masmorras", "Monstros"]:
            Tag.objects.create(name=name, campaign=instance)

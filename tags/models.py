from django.db import models
from django.utils.text import slugify
from campaign.models import Campaign


class Tag(models.Model):
    name = models.CharField(max_length=255, help_text="Nome da Tag")
    slug = models.SlugField(unique=True, blank=True)
    campaign = models.ForeignKey(Campaign, null=True, on_delete=models.CASCADE, related_name='tags', db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

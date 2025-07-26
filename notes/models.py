from django.db import models
from campaign.models import Campaign
from tags.models import Tag


class Note(models.Model):
    name = models.CharField(max_length=255, help_text="Nome")
    image = models.ImageField(upload_to='notes/', null=True, blank=True, help_text="Imagem")
    tag = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL, related_name='notes', db_index=True)
    description = models.TextField(null=True, blank=True, help_text="Descrição")
    fixed = models.BooleanField(default=False, db_index=True)
    campaign = models.ForeignKey(Campaign, null=True, on_delete=models.CASCADE, related_name='notes', db_index=True)

    def __str__(self):
        return self.name

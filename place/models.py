from django.db import models
from campaign.models import Campaign

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=255, help_text="Nome")
    image = models.ImageField(upload_to='places/', null=True, blank=True, help_text="Imagem")
    fixed = models.BooleanField(default=False, help_text="Fixo")
    campaign = models.ForeignKey(Campaign, null=True, on_delete=models.CASCADE, related_name='places', help_text="Campanha")
    history = models.TextField( null=True, blank=True, help_text="História")
    description = models.TextField( null=True, blank=True, help_text="Descrição")

    def __str__(self):
        return self.name

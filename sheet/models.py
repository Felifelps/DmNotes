from django.db import models
from campaign.models import Campaign

# Create your models here.
class Sheet(models.Model):
    name = models.CharField(max_length=255, help_text="Nome da ficha")
    image = models.ImageField(upload_to='sheets/', null=True, blank=True, help_text="Imagem da ficha")
    fixed = models.BooleanField(default=False, help_text="Fixo")
    campaign = models.ForeignKey(Campaign, null=True, on_delete=models.CASCADE, related_name='sheets', help_text="Campanha")
    history = models.TextField(null=True, blank=True, help_text="História da ficha")
    description = models.TextField(null=True, blank=True, help_text="Descrição da ficha")

    def __str__(self):
        return self.name
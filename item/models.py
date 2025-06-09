from django.db import models
from campaign.models import Campaign

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255, help_text="Nome do item")
    image = models.ImageField(upload_to='items/', null=True, blank=True, help_text="Imagem do item")
    fixed = models.BooleanField(default=False, help_text="Fixo")
    campaign = models.ForeignKey(Campaign, null=True, on_delete=models.CASCADE, related_name='items', help_text="Campanha")
    history = models.TextField(null=True, blank=True, help_text="História do item")
    description = models.TextField(null=True, blank=True, help_text="Descrição do item")

    def __str__(self):
        return self.name

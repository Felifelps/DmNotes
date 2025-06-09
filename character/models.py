from django.db import models
from campaign.models import Campaign

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=255, help_text="Nome do personagem")
    image = models.ImageField(upload_to='characters/', null=True, blank=True, help_text="Imagem do personagem")
    fixed = models.BooleanField(default=False, help_text="Fixo")
    campaign = models.ForeignKey(Campaign, null=True, blank=True, on_delete=models.CASCADE, related_name='characters', help_text="Campanha")
    history = models.TextField(null=True, blank=True, help_text="História do personagem")
    description = models.TextField(null=True, blank=True, help_text="Descrição do personagem")

    def __str__(self):
        return self.name

from django.db import models
from campaign.models import Campaign

# Create your models here.
class Dungeon(models.Model):
    name = models.CharField(max_length=255, help_text="Nome do masmorra")
    image = models.ImageField(upload_to='dungeons/', null=True, blank=True, help_text="Imagem da masmorra")
    fixed = models.BooleanField(default=False, help_text="Fixo")
    campaign = models.ForeignKey(Campaign, null=True, on_delete=models.CASCADE, related_name='dungeons', help_text="Campanha")
    history = models.TextField(null=True, blank=True, help_text="História da masmorra")
    description = models.TextField(null=True, blank=True, help_text="Descrição da masmorra")

    def __str__(self):
        return self.name

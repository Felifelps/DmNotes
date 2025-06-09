from django.db import models
from campaign.models import Campaign

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255, help_text="Título do evento")
    image = models.ImageField(upload_to='events/', null=True, blank=True, help_text="Imagem do evento")
    campaign = models.ForeignKey(Campaign, null=True, on_delete=models.CASCADE, related_name='events', help_text="Campanha")
    fixed = models.BooleanField(default=False, help_text="Fixo")
    history = models.TextField(null=True, blank=True, help_text="História do evento")
    description = models.TextField(null=True, blank=True, help_text="Descrição do evento")

    def __str__(self):
        return self.title
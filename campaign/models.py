from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Campaign(models.Model):
    name = models.CharField(max_length=255, help_text="Nome da campanha")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Usuário responsável pela campanha")
    description = models.TextField(null=True, blank=True, help_text="Descrição da campanha")
    history = models.TextField(null=True, blank=True, help_text="História da campanha")

    def __str__(self):
        return self.name

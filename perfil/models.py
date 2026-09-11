from django.db import models
from skills.models import Skill


class PerfilTecnico(models.Model):
    class Nivel(models.TextChoices):
        BASICO = "basico", "Básico"
        INTERMEDIARIO = "intermediario", "Intermediário"
        AVANCADO = "avancado", "Avançado"

    skill = models.OneToOneField(Skill, on_delete=models.CASCADE, related_name="perfil")
    nivel = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.BASICO)

    def __str__(self):
        return f"{self.skill} ({self.nivel})"
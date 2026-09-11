from django.db import models
from vagas.models import Vaga


class Skill(models.Model):
    nome_normalizado = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome_normalizado


class VagaSkill(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, related_name="skills_encontradas")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="vagas_relacionadas")
    ocorrencias = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("vaga", "skill")

    def __str__(self):
        return f"{self.skill} em {self.vaga}"
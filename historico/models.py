from django.db import models
from skills.models import Skill


class HistoricoSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="historico")
    periodo = models.DateField()
    contagem = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("skill", "periodo")
        ordering = ["periodo"]

    def __str__(self):
        return f"{self.skill} - {self.periodo}: {self.contagem}"
from django.db import models
from vagas.models import Vaga


class Candidatura(models.Model):
    class Status(models.TextChoices):
        QUERO_APLICAR = "quero_aplicar", "Quero aplicar"
        APLICADO = "aplicado", "Aplicado"
        ENTREVISTA = "entrevista", "Em entrevista"
        RECUSADO = "recusado", "Recusado"
        ACEITO = "aceito", "Aceito"

    vaga = models.OneToOneField(Vaga, on_delete=models.CASCADE, related_name="candidatura")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.QUERO_APLICAR)
    notas = models.TextField(blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vaga.titulo} — {self.get_status_display()}"
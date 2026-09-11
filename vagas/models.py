from django.db import models


class Fonte(models.Model):
    nome= models.CharField(max_length=50)
    url_base = models.URLField()

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    class Nivel(models.TextChoices):
        JUNIOR = "junior", "Júnior"
        PLENO = "pleno", "Pleno"
        SENIOR = "senior", "Sênior"
        NAO_INFORMADO = "nao_informado", "Não informado"

    fonte = models.ForeignKey(Fonte, on_delete=models.CASCADE, related_name="vagas")
    id_externo = models.CharField(max_length=100)
    titulo = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    descricao_bruta = models.TextField()
    url = models.URLField()
    nivel = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.NAO_INFORMADO)
    data_publicacao = models.DateField(null=True, blank=True)
    coletado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("fonte", "id_externo")

    def __str__(self):
        return f"{self.titulo} ({self.empresa})"
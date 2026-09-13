from rest_framework import serializers
from .models import Candidatura


class CandidaturaSerializer(serializers.ModelSerializer):
    vaga_titulo = serializers.CharField(source="vaga.titulo", read_only=True)
    vaga_empresa = serializers.CharField(source="vaga.empresa", read_only=True)
    vaga_url = serializers.CharField(source="vaga.url", read_only=True)

    class Meta:
        model = Candidatura
        fields = ["id", "vaga", "vaga_titulo", "vaga_empresa", "vaga_url", "status", "notas", "atualizado_em"]
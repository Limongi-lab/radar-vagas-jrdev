from rest_framework import serializers
from .models import PerfilTecnico


class PerfilTecnicoSerializer(serializers.ModelSerializer):
    skill_nome = serializers.CharField(source="skill.nome_normalizado", read_only=True)

    class Meta:
        model = PerfilTecnico
        fields = ["id", "skill", "skill_nome", "nivel"]
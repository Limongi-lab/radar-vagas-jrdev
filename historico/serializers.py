from rest_framework import serializers
from .models import HistoricoSkill


class HistoricoSkillSerializer(serializers.ModelSerializer):
    skill_nome = serializers.CharField(source="skill.nome_normalizado", read_only=True)

    class Meta:
        model = HistoricoSkill
        fields = ["id", "skill", "skill_nome", "periodo", "contagem"]
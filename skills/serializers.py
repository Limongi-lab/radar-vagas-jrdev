from rest_framework import serializers
from .models import Skill, VagaSkill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class VagaSkillSerializer(serializers.ModelSerializer):
    skill = serializers.StringRelatedField()
    vaga = serializers.StringRelatedField()

    class Meta:
        model = VagaSkill
        fields = "__all__"
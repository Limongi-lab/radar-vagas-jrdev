from rest_framework import viewsets
from .models import Skill, VagaSkill
from .serializers import SkillSerializer, VagaSkillSerializer


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all().order_by("nome_normalizado")
    serializer_class = SkillSerializer


class VagaSkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VagaSkill.objects.all()
    serializer_class = VagaSkillSerializer
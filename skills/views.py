from datetime import timedelta

from django.db.models import Count, Sum
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Skill, VagaSkill
from .serializers import SkillSerializer, VagaSkillSerializer
from perfil.models import PerfilTecnico


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all().order_by("nome_normalizado")
    serializer_class = SkillSerializer


class VagaSkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VagaSkill.objects.all()
    serializer_class = VagaSkillSerializer


class SkillRankingView(APIView):
    def get(self, request):
        qs = VagaSkill.objects.all()

        dias = request.query_params.get("dias")
        if dias:
            data_limite = timezone.now() - timedelta(days=int(dias))
            qs = qs.filter(vaga__coletado_em__gte=data_limite)

        nivel = request.query_params.get("nivel")
        if nivel:
            qs = qs.filter(vaga__nivel=nivel)

        ranking = (
            qs.values("skill__nome_normalizado")
            .annotate(total_vagas=Count("vaga", distinct=True), total_ocorrencias=Sum("ocorrencias"))
            .order_by("-total_vagas")
        )
        return Response(list(ranking))


class SkillGapView(APIView):
    def get(self, request):
        limite = int(request.query_params.get("limite", 15))

        ranking = (
            VagaSkill.objects.values("skill__id", "skill__nome_normalizado")
            .annotate(total_vagas=Count("vaga", distinct=True))
            .order_by("-total_vagas")[:limite]
        )
        skills_no_perfil = set(PerfilTecnico.objects.values_list("skill_id", flat=True))

        gap = [
            {"skill": item["skill__nome_normalizado"], "total_vagas": item["total_vagas"]}
            for item in ranking
            if item["skill__id"] not in skills_no_perfil
        ]
        return Response(gap)
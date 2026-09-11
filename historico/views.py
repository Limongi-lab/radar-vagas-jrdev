from rest_framework import viewsets
from .models import HistoricoSkill
from .serializers import HistoricoSkillSerializer


class HistoricoSkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HistoricoSkill.objects.all()
    serializer_class = HistoricoSkillSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        skill = self.request.query_params.get("skill")
        if skill:
            queryset = queryset.filter(skill__nome_normalizado__iexact=skill)
        return queryset
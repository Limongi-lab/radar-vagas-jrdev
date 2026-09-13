from rest_framework import viewsets
from .models import Candidatura
from .serializers import CandidaturaSerializer


class CandidaturaViewSet(viewsets.ModelViewSet):
    queryset = Candidatura.objects.all().order_by("-atualizado_em")
    serializer_class = CandidaturaSerializer
from rest_framework import viewsets
from .models import Fonte, Vaga
from .serializers import FonteSerializer, VagaSerializer


class FonteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fonte.objects.all()
    serializer_class = FonteSerializer


class VagaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = VagaSerializer

    def get_queryset(self):
        queryset = Vaga.objects.all().order_by("-coletado_em")
        fonte = self.request.query_params.get("fonte")
        nivel = self.request.query_params.get("nivel")
        if fonte:
            queryset = queryset.filter(fonte__nome__iexact=fonte)
        if nivel:
            queryset = queryset.filter(nivel=nivel)
        return queryset
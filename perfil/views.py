from rest_framework import viewsets
from .models import PerfilTecnico
from .serializers import PerfilTecnicoSerializer


class PerfilTecnicoViewSet(viewsets.ModelViewSet):
    queryset = PerfilTecnico.objects.all()
    serializer_class = PerfilTecnicoSerializer
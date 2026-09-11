from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from vagas.views import FonteViewSet, VagaViewSet
from skills.views import SkillViewSet, VagaSkillViewSet
from perfil.views import PerfilTecnicoViewSet
from historico.views import HistoricoSkillViewSet

router = DefaultRouter()
router.register("fontes", FonteViewSet)
router.register("vagas", VagaViewSet, basename="vaga")
router.register("skills", SkillViewSet)
router.register("vaga-skills", VagaSkillViewSet)
router.register("perfil", PerfilTecnicoViewSet)
router.register("historico", HistoricoSkillViewSet, basename="historico")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
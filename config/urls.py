from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from vagas.views import FonteViewSet, VagaViewSet
from skills.views import SkillViewSet, VagaSkillViewSet, SkillRankingView, SkillGapView
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
    path("api/skills/ranking/", SkillRankingView.as_view()),
    path("api/skills/gap/", SkillGapView.as_view()),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
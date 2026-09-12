import pytest
from skills.models import Skill
from perfil.models import PerfilTecnico


@pytest.mark.django_db
def test_perfil_tecnico_um_por_skill():
    skill = Skill.objects.create(nome_normalizado="Python")
    PerfilTecnico.objects.create(skill=skill, nivel="avancado")
    with pytest.raises(Exception):
        PerfilTecnico.objects.create(skill=skill, nivel="basico")
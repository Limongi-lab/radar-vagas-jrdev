import pytest
from skills.models import Skill
from skills.extracao import extrair_skills


@pytest.mark.django_db
def test_extrair_skills_encontra_termo_no_texto():
    Skill.objects.create(nome_normalizado="Python")
    Skill.objects.create(nome_normalizado="React")
    resultado = extrair_skills("Vaga para dev Python com experiência em Python e React")
    nomes = {skill.nome_normalizado: ocorrencias for skill, ocorrencias in resultado.items()}
    assert nomes["Python"] == 2
    assert nomes["React"] == 1


@pytest.mark.django_db
def test_extrair_skills_ignora_substring_parcial():
    Skill.objects.create(nome_normalizado="Java")
    resultado = extrair_skills("Vaga para dev JavaScript")
    assert list(resultado.items()) == []

@pytest.mark.django_db
def test_extrair_skills_reconhece_sinonimo():
    Skill.objects.create(nome_normalizado="React")
    resultado = extrair_skills("Vaga para dev ReactJS")
    nomes = {skill.nome_normalizado: oc for skill, oc in resultado.items()}
    assert nomes["React"] == 1
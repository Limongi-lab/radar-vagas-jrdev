import pytest
from vagas.models import Fonte, Vaga
from vagas.niveis import classificar_nivel


@pytest.mark.django_db
def test_fonte_str():
    fonte = Fonte.objects.create(nome="Remotive", url_base="https://remotive.com/api/remote-jobs")
    assert str(fonte) == "Remotive"


@pytest.mark.django_db
def test_vaga_unique_por_fonte_e_id_externo():
    fonte = Fonte.objects.create(nome="Remotive", url_base="https://remotive.com/api/remote-jobs")
    Vaga.objects.create(
        fonte=fonte, id_externo="123", titulo="Dev", empresa="X",
        descricao_bruta="desc", url="https://x.com",
    )
    with pytest.raises(Exception):
        Vaga.objects.create(
            fonte=fonte, id_externo="123", titulo="Dev 2", empresa="Y",
            descricao_bruta="desc2", url="https://y.com",
        )


def test_classificar_nivel_junior():
    assert classificar_nivel("Desenvolvedor Júnior Python") == "junior"


def test_classificar_nivel_senior():
    assert classificar_nivel("Senior Backend Engineer") == "senior"


def test_classificar_nivel_sem_info():
    assert classificar_nivel("Backend Engineer") == "nao_informado"
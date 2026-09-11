import re
from collections import Counter
from .models import Skill


def extrair_skills(texto):
    contagem = Counter()
    texto_lower = texto.lower()
    for skill in Skill.objects.all():
        nome = skill.nome_normalizado
        padrao = r"(?<!\w)" + re.escape(nome.lower()) + r"(?!\w)"
        ocorrencias = len(re.findall(padrao, texto_lower))
        if ocorrencias:
            contagem[skill] = ocorrencias
    return contagem
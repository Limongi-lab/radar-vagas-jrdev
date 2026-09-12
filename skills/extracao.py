import re
from collections import Counter
from .models import Skill
from .sinonimos import SINONIMOS


def extrair_skills(texto):
    contagem = Counter()
    texto_lower = texto.lower()
    for skill in Skill.objects.all():
        nomes_para_buscar = [skill.nome_normalizado] + SINONIMOS.get(skill.nome_normalizado, [])
        ocorrencias = 0
        for nome in nomes_para_buscar:
            padrao = r"(?<!\w)" + re.escape(nome.lower()) + r"(?!\w)"
            ocorrencias += len(re.findall(padrao, texto_lower))
        if ocorrencias:
            contagem[skill] = ocorrencias
    return contagem
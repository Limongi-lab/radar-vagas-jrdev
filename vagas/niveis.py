import re

PADRAO_JUNIOR = re.compile(
    r"j[uú]nior|jr\.?\b|entry.level|estagi[aá]rio|trainee|graduate|associate",
    re.IGNORECASE,
)
PADRAO_SENIOR = re.compile(r"s[êe]nior|sr\.?\b|lead|principal|staff|head of", re.IGNORECASE)
PADRAO_PLENO = re.compile(r"pleno|mid.level|intermediate", re.IGNORECASE)


def classificar_nivel(texto):
    if PADRAO_JUNIOR.search(texto):
        return "junior"
    if PADRAO_SENIOR.search(texto):
        return "senior"
    if PADRAO_PLENO.search(texto):
        return "pleno"
    return "nao_informado"
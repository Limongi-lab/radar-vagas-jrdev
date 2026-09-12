from datetime import datetime

import requests
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.html import strip_tags

from vagas.models import Fonte, Vaga
from vagas.niveis import classificar_nivel
from skills.extracao import extrair_skills
from skills.models import VagaSkill

ADZUNA_URL = "https://api.adzuna.com/v1/api/jobs/br/search/1"


class Command(BaseCommand):
    help = "Coleta vagas de TI no Brasil via Adzuna, classifica o nível e extrai as skills mencionadas"

    def handle(self, *args, **options):
        fonte, _ = Fonte.objects.get_or_create(
            nome="Adzuna",
            defaults={"url_base": ADZUNA_URL},
        )

        params = {
            "app_id": settings.ADZUNA_APP_ID,
            "app_key": settings.ADZUNA_APP_KEY,
            "results_per_page": 50,
            "category": "it-jobs",
            "content-type": "application/json",
        }
        resposta = requests.get(ADZUNA_URL, params=params, timeout=30)
        resposta.raise_for_status()
        jobs = resposta.json().get("results", [])

        contagem_nivel = {"junior": 0, "pleno": 0, "senior": 0, "nao_informado": 0}

        for job in jobs:
            titulo = job.get("title", "")
            descricao_limpa = strip_tags(job.get("description", ""))
            nivel = classificar_nivel(f"{titulo} {descricao_limpa}")
            contagem_nivel[nivel] += 1

            data_publicacao = None
            try:
                data_publicacao = datetime.fromisoformat(
                    job["created"].replace("Z", "+00:00")
                ).date()
            except (KeyError, ValueError):
                pass

            vaga, _ = Vaga.objects.update_or_create(
                fonte=fonte,
                id_externo=str(job["id"]),
                defaults={
                    "titulo": titulo[:255],
                    "empresa": job.get("company", {}).get("display_name", "")[:255],
                    "descricao_bruta": descricao_limpa,
                    "url": job.get("redirect_url", ""),
                    "nivel": nivel,
                    "data_publicacao": data_publicacao,
                },
            )

            texto_para_analise = f"{vaga.titulo} {vaga.descricao_bruta}"
            for skill, ocorrencias in extrair_skills(texto_para_analise).items():
                VagaSkill.objects.update_or_create(
                    vaga=vaga, skill=skill, defaults={"ocorrencias": ocorrencias}
                )

        self.stdout.write(self.style.SUCCESS(f"Coleta concluída: {len(jobs)} vagas processadas — {contagem_nivel}"))
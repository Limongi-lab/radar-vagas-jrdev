from django.core.management.base import BaseCommand
from skills.models import Skill
from perfil.models import PerfilTecnico

MINHAS_SKILLS = [
    "Python", "JavaScript", "Java", "SQL", "HTML", "CSS",
    "React", "Node.js", "MongoDB", "SQLite", "Git",
]


class Command(BaseCommand):
    help = "Popula o PerfilTecnico com as skills atuais"

    def handle(self, *args, **options):
        criadas = 0
        for nome in MINHAS_SKILLS:
            try:
                skill = Skill.objects.get(nome_normalizado=nome)
            except Skill.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Skill '{nome}' não existe no catálogo, pulei"))
                continue
            _, created = PerfilTecnico.objects.get_or_create(skill=skill)
            if created:
                criadas += 1
        self.stdout.write(self.style.SUCCESS(f"{criadas} skills adicionadas ao perfil"))
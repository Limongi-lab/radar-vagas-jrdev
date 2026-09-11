from django.core.management.base import BaseCommand
from skills.models import Skill

SKILLS_INICIAIS = [
    "Python", "JavaScript", "TypeScript", "Java", "C#", "PHP", "Ruby",
    "Django", "Flask", "FastAPI", "Spring", "Laravel", "Rails", ".NET",
    "React", "Vue", "Angular", "Node.js", "Express", "jQuery",
    "HTML", "CSS", "Bootstrap", "Tailwind",
    "SQL", "PostgreSQL", "MySQL", "MongoDB", "Redis", "SQLite",
    "REST", "GraphQL", "Swagger", "OAuth", "Microservices",
    "Docker", "Kubernetes", "AWS", "Azure", "GCP", "Terraform", "Jenkins",
    "Git", "Linux", "CI/CD",
    "Scrum", "Agile", "TDD",
    "pytest", "Jest", "Webpack",
    "Kafka", "Elasticsearch",
]


class Command(BaseCommand):
    help = "Popula o catálogo inicial de skills"

    def handle(self, *args, **options):
        criadas = 0
        for nome in SKILLS_INICIAIS:
            _, created = Skill.objects.get_or_create(nome_normalizado=nome)
            if created:
                criadas += 1
        self.stdout.write(self.style.SUCCESS(f"{criadas} skills novas de {len(SKILLS_INICIAIS)} no total"))
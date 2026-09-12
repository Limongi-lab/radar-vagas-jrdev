from django.core.management.base import BaseCommand
from django.db.models import Count
from django.utils import timezone

from skills.models import VagaSkill
from historico.models import HistoricoSkill


class Command(BaseCommand):
    help = "Gera um snapshot do histórico de demanda de skills na data atual"

    def handle(self, *args, **options):
        hoje = timezone.now().date()
        ranking = (
            VagaSkill.objects.values("skill_id")
            .annotate(total=Count("vaga", distinct=True))
        )

        criados = 0
        for item in ranking:
            _, created = HistoricoSkill.objects.update_or_create(
                skill_id=item["skill_id"],
                periodo=hoje,
                defaults={"contagem": item["total"]},
            )
            if created:
                criados += 1

        self.stdout.write(
            self.style.SUCCESS(f"Snapshot de {hoje}: {len(ranking)} skills registradas ({criados} novas)")
        )
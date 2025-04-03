from django.core.management.base import BaseCommand
from legacy.models import TipOpo, Opo, ClassOpasnosti
from opo.models import TypeOPO, OPO, HazardClass  # Подкорректируй под своё приложение


class Command(BaseCommand):
    help = 'Импорт данных из MSSQL (наследие) в PostgreSQL (новая структура)'

    def handle(self, *args, **options):
        self.import_tipopo()
        self.import_class_opasnosti()
        self.import_opo()

    def import_tipopo(self):
        for tip in TipOpo.objects.using('mssql').all():
            TypeOPO.objects.update_or_create(
                id=tip.id,
                defaults={
                    'name': tip.txt,
                    'short_name': tip.txt_short,
                    'reg_number': tip.reg_number
                }
            )
        self.stdout.write(self.style.SUCCESS('Импорт TipOpo завершён.'))

    def import_class_opasnosti(self):
        for hazard in ClassOpasnosti.objects.using('mssql').all():
            HazardClass.objects.update_or_create(
                id=hazard.id,
                defaults={'name': hazard.txt}
            )
        self.stdout.write(self.style.SUCCESS('Импорт ClassOpasnosti завершён.'))

    def import_opo(self):
        for old_opo in Opo.objects.using('mssql').all():
            try:
                type_instance = TypeOPO.objects.get(id=old_opo.id_type_opo)
                OPO.objects.update_or_create(
                    id=old_opo.id_opo,
                    defaults={
                        'type': type_instance,
                        'structural_unit': old_opo.id_strukturn_podrazd,
                        'name': old_opo.txt,
                        'short_name': old_opo.txt_short,
                        'reg_number': old_opo.reg_number
                    }
                )
            except TypeOPO.DoesNotExist:
                self.stdout.write(self.style.WARNING(
                    f"Пропущен OPO {old_opo.id_opo}: не найден тип {old_opo.id_type_opo}"
                ))
        self.stdout.write(self.style.SUCCESS('Импорт OPO завершён.'))

import json

from django.core.management import BaseCommand

from campaign.models import Campaign
from sheet.models import Sheet


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
        )

        parser.add_argument(
            'delete_all',
            type=bool,
            help='Deletar todos os objetos antes de importar'
        )

    def handle(self, *args,**options):
        file_name = options['file_name']

        if options['delete_all']:
            Sheet.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Todos os objetos foram deletados.'))

        if not file_name.endswith('.json'):
            self.stdout.write(self.style.ERROR('O arquivo deve ser um JSON.'))
            return

        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for sheet in data:
            sheet.pop('id', None)
            sheet.pop('image_path', None)
            sheet['campaign'] = Campaign.objects.get(
                pk=sheet.get('campaign_id', 1)  # Default to campaign with ID 1 if not specified
            )

            try:
                Sheet.objects.create(
                    **sheet
                )
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Erro ao importar personagem {sheet.get('name', 'desconhecido')}: {e}"))
                continue

            # Só pra printar bonito
            self.stdout.write(self.style.NOTICE(sheet['name']))

        # Só pra printar bonito
        self.stdout.write(self.style.SUCCESS('sheets importados com sucesso!'))

import json

from django.core.management import BaseCommand

from campaign.models import Campaign
from event.models import Event


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com atores'
        )

        parser.add_argument(
            'delete_all',
            type=bool,
            help='Deletar todos os objetos antes de importar'
        )

    def handle(self, *args,**options):
        file_name = options['file_name']

        if options['delete_all']:
            Event.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Todos os objetos foram deletados.'))

        if not file_name.endswith('.json'):
            self.stdout.write(self.style.ERROR('O arquivo deve ser um JSON.'))
            return

        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for event in data:
            event.pop('id', None)
            event.pop('image_path', None)
            event['campaign'] = Campaign.objects.get(
                pk=event.get('campaign_id', 1)  # Default to campaign with ID 1 if not specified
            )

            try:
                event.objects.create(
                    **event
                )
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Erro ao importar personagem {event.get('name', 'desconhecido')}: {e}"))
                continue

            # Só pra printar bonito
            self.stdout.write(self.style.NOTICE(event['name']))

        # Só pra printar bonito
        self.stdout.write(self.style.SUCCESS('events importados com sucesso!'))

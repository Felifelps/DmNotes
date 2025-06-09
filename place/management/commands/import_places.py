import json

from django.core.management import BaseCommand

from campaign.models import Campaign
from place.models import Place


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

        if not file_name.endswith('.json'):
            self.stdout.write(self.style.ERROR('O arquivo deve ser um JSON.'))
            return

        if options['delete_all']:
            Place.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Todos os objetos foram deletados.'))

        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for place in data:
            place.pop('id', None)
            place.pop('image_path', None)
            place['campaign'] = Campaign.objects.get(
                pk=place.get('campaign_id', 1)  # Default to campaign with ID 1 if not specified
            )

            try:
                Place.objects.create(
                    **place
                )
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Erro ao importar personagem {place.get('name', 'desconhecido')}: {e}"))
                continue

            # Só pra printar bonito
            self.stdout.write(self.style.NOTICE(place['name']))

        # Só pra printar bonito
        self.stdout.write(self.style.SUCCESS('places importados com sucesso!'))

import json

from django.core.management import BaseCommand

from campaign.models import Campaign
from item.models import Item


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
            Item.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Todos os objetos foram deletados.'))

        if not file_name.endswith('.json'):
            self.stdout.write(self.style.ERROR('O arquivo deve ser um JSON.'))
            return

        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            item.pop('id', None)
            item.pop('image_path', None)
            item['campaign'] = Campaign.objects.get(
                pk=item.get('campaign_id', 1)  # Default to campaign with ID 1 if not specified
            )

            try:
                Item.objects.create(
                    **item
                )
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Erro ao importar personagem {item.get('name', 'desconhecido')}: {e}"))
                continue

            # Só pra printar bonito
            self.stdout.write(self.style.NOTICE(item['name']))

        # Só pra printar bonito
        self.stdout.write(self.style.SUCCESS('items importados com sucesso!'))

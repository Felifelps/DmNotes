from django.apps import AppConfig


class DungeonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dungeon'

    def ready(self) -> None:
        import dungeon.signals

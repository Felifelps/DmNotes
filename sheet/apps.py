from django.apps import AppConfig


class SheetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sheet'

    def ready(self) -> None:
        import sheet.signals

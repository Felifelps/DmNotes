from django.apps import AppConfig


class CampaignConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'campaign'

    def ready(self) -> None:
        import campaign.signals

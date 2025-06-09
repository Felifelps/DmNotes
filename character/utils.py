from django.urls import reverse
from campaign.utils import CampaignGenericViewMixin

class CharacterGenericViewMixin(CampaignGenericViewMixin):

    def get_success_url(self):
        return reverse('character_list', kwargs={'campaign_pk': self.campaign.pk})
    
    def get_queryset(self):
        return self.campaign.characters.all()

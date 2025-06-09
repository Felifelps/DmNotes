from django.urls import reverse
from campaign.utils import CampaignGenericViewMixin

class DungeonGenericViewMixin(CampaignGenericViewMixin):

    def get_success_url(self):
        return reverse('dungeon_list', kwargs={'campaign_pk': self.campaign.pk})
    
    def get_queryset(self):
        return self.campaign.dungeons.all()

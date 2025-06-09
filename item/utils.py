from django.urls import reverse
from campaign.utils import CampaignGenericViewMixin

class ItemGenericViewMixin(CampaignGenericViewMixin):

    def get_success_url(self):
        return reverse('item_list', kwargs={'campaign_pk': self.campaign.pk})
    
    def get_queryset(self):
        return self.campaign.items.all()

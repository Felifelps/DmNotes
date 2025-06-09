from django.urls import reverse
from campaign.utils import CampaignGenericViewMixin

class SheetGenericViewMixin(CampaignGenericViewMixin):

    def get_success_url(self):
        return reverse('sheet_list', kwargs={'campaign_pk': self.campaign.pk})
    
    def get_queryset(self):
        return self.campaign.sheets.all()

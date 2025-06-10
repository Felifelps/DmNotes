from django.urls import reverse
from django.shortcuts import get_object_or_404
from campaign.models import Campaign
from campaign.utils import CampaignGenericViewMixin

class NoteGenericViewMixin(CampaignGenericViewMixin):

    def get_success_url(self):
        return reverse('campaign_detail', kwargs={'campaign_pk': self.campaign.pk})
    
    def get_queryset(self):
        return self.campaign.notes.all()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        campaign = get_object_or_404(Campaign, pk=self.kwargs['campaign_pk'])
        kwargs['campaign'] = campaign
        return kwargs

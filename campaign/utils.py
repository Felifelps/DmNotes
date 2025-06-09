from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from campaign.models import Campaign

class CampaignGenericViewMixin:
    def dispatch(self, request, *args, **kwargs):
        self.campaign = get_object_or_404(Campaign, pk=self.kwargs['campaign_pk'])

        if not self.campaign.user == request.user:
            return redirect('campaign_list')

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = self.campaign
        return context

    def form_valid(self, form):
        if isinstance(self, CreateView):
            form.instance.campaign = self.campaign
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('character_list', kwargs={'campaign_pk': self.campaign.pk})

class CampaignDetailMixin:
    def dispatch(self, request, *args, **kwargs):
        self.campaign = get_object_or_404(Campaign, pk=self.kwargs['campaign_pk'])

        if not self.campaign.user == request.user:
            return redirect('campaign_list')

        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(Campaign, pk=self.kwargs['campaign_pk'])

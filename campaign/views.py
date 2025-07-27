from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from campaign.models import Campaign
from campaign.forms import CampaignForm
from campaign.utils import CampaignDetailMixin

from notes.models import Note
from notes.forms import NoteForm


class CampaignListView(LoginRequiredMixin, ListView):
    model = Campaign
    template_name = 'campaign_list.html'
    context_object_name = 'campaigns'

    def get_queryset(self):
        return Campaign.objects.filter(user=self.request.user).order_by('-id')


class CampaignDetailView(LoginRequiredMixin, CampaignDetailMixin, DetailView):
    model = Campaign
    template_name = 'campaign_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        campaign = self.get_object()

        context['fixeds'] = Note.objects.filter(campaign=campaign, fixed=True)
        context['notes'] = Note.objects.filter(campaign=campaign, fixed=False)
        context['tags'] = self.campaign.tags.all()
        context['note_form'] = NoteForm(campaign=campaign)

        return context


class CampaignCreateView(LoginRequiredMixin, CreateView):
    model = Campaign
    form_class = CampaignForm
    template_name = 'campaign_create.html'

    def get_success_url(self):
        return reverse('campaign_detail', args=[self.object.pk])

    def form_valid(self, form):
        if isinstance(self, CreateView):
            form.instance.user = self.request.user
        return super().form_valid(form)


class CampaignUpdateView(LoginRequiredMixin, CampaignDetailMixin, UpdateView):
    model = Campaign
    form_class = CampaignForm
    template_name = 'campaign_update.html'

    def get_success_url(self):
        return reverse('campaign_detail', args=[self.object.pk])


class CampaignDeleteView(LoginRequiredMixin, CampaignDetailMixin, DeleteView):
    model = Campaign
    template_name = 'campaign_delete.html'
    success_url = '/'

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse
from django.http import JsonResponse

from event.models import Event
from event.forms import EventForm
from event.utils import EventGenericViewMixin

class EventToggleFixedView(View):

    def post(self, request, *args, **kwargs):
        event = Event.objects.get(pk=kwargs['pk'])
        event.fixed = not event.fixed
        event.save()

        return JsonResponse({
            'fixed': event.fixed,
            'message': 'Event fixed status updated successfully.'
        })

class EventListView(LoginRequiredMixin, EventGenericViewMixin, ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'

class EventDetailView(LoginRequiredMixin, EventGenericViewMixin, DetailView):
    model = Event
    template_name = 'event_detail.html'

class EventCreateView(LoginRequiredMixin, EventGenericViewMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event_create.html'

class EventUpdateView(LoginRequiredMixin, EventGenericViewMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event_update.html'

class EventDeleteView(LoginRequiredMixin, EventGenericViewMixin, DeleteView):
    model = Event
    template_name = 'event_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = self.object.campaign
        return context

    def get_success_url(self):
        return reverse('event_list', args=[self.object.campaign.pk])

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse
from django.http import JsonResponse

from place.models import Place
from place.forms import PlaceForm
from place.utils import PlaceGenericViewMixin

class PlaceToggleFixedView(View):

    def post(self, request, *args, **kwargs):
        place = Place.objects.get(pk=kwargs['pk'])
        place.fixed = not place.fixed
        place.save()

        return JsonResponse({
            'fixed': place.fixed,
            'message': 'Place fixed status updated successfully.'
        })

class PlaceListView(LoginRequiredMixin, PlaceGenericViewMixin, ListView):
    model = Place
    template_name = 'place_list.html'
    context_object_name = 'places'

class PlaceDetailView(LoginRequiredMixin, PlaceGenericViewMixin, DetailView):
    model = Place
    template_name = 'place_detail.html'

class PlaceCreateView(LoginRequiredMixin, PlaceGenericViewMixin, CreateView):
    model = Place
    form_class = PlaceForm
    template_name = 'place_create.html'

class PlaceUpdateView(LoginRequiredMixin, PlaceGenericViewMixin, UpdateView):
    model = Place
    form_class = PlaceForm
    template_name = 'place_update.html'

class PlaceDeleteView(LoginRequiredMixin, PlaceGenericViewMixin, DeleteView):
    model = Place
    template_name = 'place_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = self.object.campaign
        return context

    def get_success_url(self):
        return reverse('place_list', args=[self.object.campaign.pk])

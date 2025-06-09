from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse
from django.http import JsonResponse

from character.models import Character
from character.forms import CharacterForm
from character.utils import CharacterGenericViewMixin

class CharacterToggleFixedView(View):

    def post(self, request, *args, **kwargs):
        character = Character.objects.get(pk=kwargs['pk'])
        character.fixed = not character.fixed
        character.save()

        return JsonResponse({
            'fixed': character.fixed,
            'message': 'Character fixed status updated successfully.'
        })

class CharacterListView(LoginRequiredMixin, CharacterGenericViewMixin, ListView):
    model = Character
    template_name = 'character_list.html'
    context_object_name = 'characters'

class CharacterDetailView(LoginRequiredMixin, CharacterGenericViewMixin, DetailView):
    model = Character
    template_name = 'character_detail.html'

class CharacterCreateView(LoginRequiredMixin, CharacterGenericViewMixin, CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'character_create.html'

class CharacterUpdateView(LoginRequiredMixin, CharacterGenericViewMixin, UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = 'character_update.html'

class CharacterDeleteView(LoginRequiredMixin, CharacterGenericViewMixin, DeleteView):
    model = Character
    template_name = 'character_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = self.object.campaign
        return context

    def get_success_url(self):
        return reverse('character_list', args=[self.object.campaign.pk])

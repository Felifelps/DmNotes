from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse
from django.http import JsonResponse

from dungeon.models import Dungeon
from dungeon.forms import DungeonForm
from dungeon.utils import DungeonGenericViewMixin

class DungeonToggleFixedView(View):

    def post(self, request, *args, **kwargs):
        dungeon = Dungeon.objects.get(pk=kwargs['pk'])
        dungeon.fixed = not dungeon.fixed
        dungeon.save()

        return JsonResponse({
            'fixed': dungeon.fixed,
            'message': 'Dungeon fixed status updated successfully.'
        })

class DungeonListView(LoginRequiredMixin, DungeonGenericViewMixin, ListView):
    model = Dungeon
    template_name = 'dungeon_list.html'
    context_object_name = 'dungeons'

class DungeonDetailView(LoginRequiredMixin, DungeonGenericViewMixin, DetailView):
    model = Dungeon
    template_name = 'dungeon_detail.html'

class DungeonCreateView(LoginRequiredMixin, DungeonGenericViewMixin, CreateView):
    model = Dungeon
    form_class = DungeonForm
    template_name = 'dungeon_create.html'

class DungeonUpdateView(LoginRequiredMixin, DungeonGenericViewMixin, UpdateView):
    model = Dungeon
    form_class = DungeonForm
    template_name = 'dungeon_update.html'

class DungeonDeleteView(LoginRequiredMixin, DungeonGenericViewMixin, DeleteView):
    model = Dungeon
    template_name = 'dungeon_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = self.object.campaign
        return context

    def get_success_url(self):
        return reverse('dungeon_list', args=[self.object.campaign.pk])

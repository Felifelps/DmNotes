from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse
from django.http import JsonResponse

from item.models import Item
from item.forms import ItemForm
from item.utils import ItemGenericViewMixin

class ItemToggleFixedView(View):

    def post(self, request, *args, **kwargs):
        item = Item.objects.get(pk=kwargs['pk'])
        item.fixed = not item.fixed
        item.save()

        return JsonResponse({
            'fixed': item.fixed,
            'message': 'Item fixed status updated successfully.'
        })

class ItemListView(LoginRequiredMixin, ItemGenericViewMixin, ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'

class ItemDetailView(LoginRequiredMixin, ItemGenericViewMixin, DetailView):
    model = Item
    template_name = 'item_detail.html'

class ItemCreateView(LoginRequiredMixin, ItemGenericViewMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_create.html'

class ItemUpdateView(LoginRequiredMixin, ItemGenericViewMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_update.html'

class ItemDeleteView(LoginRequiredMixin, ItemGenericViewMixin, DeleteView):
    model = Item
    template_name = 'item_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = self.object.campaign
        return context

    def get_success_url(self):
        return reverse('item_list', args=[self.object.campaign.pk])

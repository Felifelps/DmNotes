from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, CreateView, DeleteView
from django.urls import reverse

from tags.models import Tag
from tags.forms import TagForm
from tags.utils import TagGenericViewMixin


class TagListView(LoginRequiredMixin, TagGenericViewMixin, ListView):
    model = Tag
    template_name = 'tag_list.html'
    context_object_name = 'tags'

class TagCreateView(LoginRequiredMixin, TagGenericViewMixin, CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag_create.html'

class TagDeleteView(LoginRequiredMixin, TagGenericViewMixin, DeleteView):
    model = Tag
    template_name = 'tag_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = self.object.campaign
        return context

    def get_success_url(self):
        return reverse('tag_list', args=[self.object.campaign.pk])

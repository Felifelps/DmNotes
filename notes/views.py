from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse
from django.http import JsonResponse

from notes.models import Note
from notes.forms import NoteForm
from notes.utils import NoteGenericViewMixin

class NoteToggleFixedView(View):

    def post(self, request, *args, **kwargs):
        note = Note.objects.get(pk=kwargs['pk'])
        note.fixed = not note.fixed
        note.save()

        return JsonResponse({
            'fixed': note.fixed,
            'message': 'Note fixed status updated successfully.'
        })

class NoteListView(LoginRequiredMixin, NoteGenericViewMixin, ListView):
    model = Note
    template_name = 'note_list.html'
    context_object_name = 'notes'

class NoteDetailView(LoginRequiredMixin, NoteGenericViewMixin, DetailView):
    model = Note
    template_name = 'note_detail.html'

class NoteCreateView(LoginRequiredMixin, NoteGenericViewMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_create.html'

class NoteUpdateView(LoginRequiredMixin, NoteGenericViewMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_update.html'

class NoteDeleteView(LoginRequiredMixin, NoteGenericViewMixin, DeleteView):
    model = Note
    template_name = 'note_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = self.object.campaign
        return context

    def get_success_url(self):
        return reverse('campaign_detail', args=[self.object.campaign.pk])

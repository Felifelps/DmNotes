from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, CreateView, DeleteView
from django.urls import reverse
from django.shortcuts import redirect
from django.http import JsonResponse

from notes.models import Note
from notes.forms import NoteForm
from notes.utils import NoteGenericViewMixin, NoteCreateOrUpdateViewMixin
from tags.models import Tag

class NoteToggleFixedView(View):
    def post(self, request, *args, **kwargs):
        note = Note.objects.get(pk=kwargs['pk'])
        note.fixed = not note.fixed
        note.save()
        return JsonResponse({'fixed': note.fixed, 'message': 'Note fixed status updated successfully.'})

class NoteCreateView(LoginRequiredMixin, NoteCreateOrUpdateViewMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_create.html'

class NoteUpdateView(LoginRequiredMixin, NoteCreateOrUpdateViewMixin, View):

    def post(self, request, *args, **kwargs):
        data = request.POST
        image = request.FILES.get('image')

        note = Note.objects.get(pk=kwargs.get('pk'))
        note.name = data.get('name')
        note.description = data.get('description')
        note.tag = Tag.objects.get(pk=data.get('tag')) if data.get('tag') else None

        if image:
            note.image = image

        note.save()

        campaign_pk = kwargs.get('campaign_pk') or note.campaign_pk
        return redirect('campaign_detail', campaign_pk=campaign_pk)


class NoteDeleteView(LoginRequiredMixin, NoteGenericViewMixin, DeleteView):
    model = Note
    template_name = 'note_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = self.object.campaign
        return context

    def get_success_url(self):
        return reverse('campaign_detail', args=[self.object.campaign.pk])

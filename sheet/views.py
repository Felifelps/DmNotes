from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse
from django.http import JsonResponse

from sheet.models import Sheet
from sheet.forms import SheetForm
from sheet.utils import SheetGenericViewMixin

class SheetToggleFixedView(View):

    def post(self, request, *args, **kwargs):
        sheet = Sheet.objects.get(pk=kwargs['pk'])
        sheet.fixed = not sheet.fixed
        sheet.save()

        return JsonResponse({
            'fixed': sheet.fixed,
            'message': 'Sheet fixed status updated successfully.'
        })

class SheetListView(LoginRequiredMixin, SheetGenericViewMixin, ListView):
    model = Sheet
    template_name = 'sheet_list.html'
    context_object_name = 'sheets'

class SheetDetailView(LoginRequiredMixin, SheetGenericViewMixin, DetailView):
    model = Sheet
    template_name = 'sheet_detail.html'

class SheetCreateView(LoginRequiredMixin, SheetGenericViewMixin, CreateView):
    model = Sheet
    form_class = SheetForm
    template_name = 'sheet_create.html'

class SheetUpdateView(LoginRequiredMixin, SheetGenericViewMixin, UpdateView):
    model = Sheet
    form_class = SheetForm
    template_name = 'sheet_update.html'

class SheetDeleteView(LoginRequiredMixin, SheetGenericViewMixin, DeleteView):
    model = Sheet
    template_name = 'sheet_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = self.object.campaign
        return context

    def get_success_url(self):
        return reverse('sheet_list', args=[self.object.campaign.pk])

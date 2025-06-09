from event.models import Event
from django import forms


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['campaign', 'fixed']
        labels = {
            'title': 'Título do Evento',
            'image': 'Imagem do Evento',
            'history': 'História do Evento',
            'description': 'Descrição do Evento',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control'},
            ),
            'history': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
        }

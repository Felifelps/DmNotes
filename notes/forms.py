from notes.models import Note
from django import forms


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        exclude = ['campaign', 'fixed']
        labels = {
            'name': 'Nome da Nota',
            'image': 'Imagem da Nota',
            'tag': 'Tag da Nota',
            'description': 'Descrição da Nota',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control'},
            ),
            'tag': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
        }

    def __init__(self, *args, **kwargs):
        campaign = kwargs.pop('campaign', None)
        super().__init__(*args, **kwargs)
        if campaign:
            self.fields['tag'].queryset = campaign.tags.all()
        else:
            self.fields['tag'].queryset = self.fields['tag'].queryset.none()

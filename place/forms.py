from place.models import Place
from django import forms


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
        exclude = ['campaign', 'fixed']
        labels = {
            'name': 'Nome do Lugar',
            'image': 'Imagem do Lugar',
            'history': 'História do Lugar',
            'description': 'Descrição do Lugar',
        }
        widgets = {
            'name': forms.TextInput(
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

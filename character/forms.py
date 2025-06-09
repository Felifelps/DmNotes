from character.models import Character
from django import forms


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'
        exclude = ['campaign', 'fixed']
        labels = {
            'name': 'Nome do personagem',
            'image': 'Imagem do personagem',
            'history': 'História do personagem',
            'description': 'Descrição do personagem',
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

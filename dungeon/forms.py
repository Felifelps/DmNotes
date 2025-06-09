from dungeon.models import Dungeon
from django import forms


class DungeonForm(forms.ModelForm):
    class Meta:
        model = Dungeon
        fields = '__all__'
        exclude = ['campaign', 'fixed']
        labels = {
            'name': 'Nome da Masmorra',
            'image': 'Imagem da Masmorra',
            'history': 'História da Masmorra',
            'description': 'Descrição da Masmorra',
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

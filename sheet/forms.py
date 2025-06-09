from sheet.models import Sheet
from django import forms


class SheetForm(forms.ModelForm):
    class Meta:
        model = Sheet
        fields = '__all__'
        exclude = ['campaign', 'fixed']
        labels = {
            'name': 'Nome da Ficha',
            'image': 'Imagem da Ficha',
            'history': 'História da Ficha',
            'description': 'Descrição da Ficha',
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

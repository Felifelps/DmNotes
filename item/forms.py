from item.models import Item
from django import forms


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['campaign', 'fixed']
        labels = {
            'name': 'Nome do Item',
            'image': 'Imagem do Item',
            'history': 'História do Item',
            'description': 'Descrição do Item',
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

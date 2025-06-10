from tags.models import Tag
from django import forms


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        exclude = ['campaign', 'slug']
        labels = {
            'name': 'Nome da Tag',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }

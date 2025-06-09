from campaign.models import Campaign
from django import forms


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = '__all__'

        labels = {
            'name': 'Nome da campanha',
            'history': 'História da campanha',
            'description': 'Descrição da campanha',
        }
        exclude = ['user']

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'history': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
        }

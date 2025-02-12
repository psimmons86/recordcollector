from django import forms
from .models import Listening

class ListeningForm(forms.ModelForm):
    class Meta:
        model = Listening
        fields = ['date', 'time']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

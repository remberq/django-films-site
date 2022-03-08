from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    """Form to email sub"""

    class Meta:
        model = Contact
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(attrs={'class': 'editContent', 'placeholder': 'Your Email ...'})
        }
        labels = {
            'email': ''
        }
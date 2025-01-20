from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        """
        A form for submitting contact details and a message.
        """
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5})
        }

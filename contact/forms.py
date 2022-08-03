"Imported"
from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    """A class for Contact form"""

    class Meta:
        """Meta for contact form"""
        model = ContactMessage()
        fields = '__all__'

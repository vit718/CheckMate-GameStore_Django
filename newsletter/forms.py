"Imported"
from django import forms
from crispy_forms.helper import FormHelper
from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    """A class for newsletter form"""

    sub_form = forms.BooleanField(initial=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # Remove form label
        self.fields['email'].label = False
        self.fields['sub_form'].label = (
            "Please check this box if you want to continue")

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'})
        )

    class Meta:
        """Meta for email field"""
        model = Subscriber
        fields = ["email"]

        def clean_email(self):
            """Gets valid data only"""
            email = self.cleaned_data.get("email")

            return email

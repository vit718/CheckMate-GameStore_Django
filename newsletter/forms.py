from django import forms
from .models import Subscriber
from crispy_forms.helper import FormHelper


class SubscriberForm(forms.ModelForm):

    sub_form = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['email'].label = False

    class Meta:
        model = Subscriber
        fields = ["email"]

        def clean_email(self):
            email = self.cleaned_data.get("email")

            return email
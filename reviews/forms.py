"""imported"""
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """A form to add a new review"""
    class Meta:
        model = Review
        fields = ('comment', 'rating')


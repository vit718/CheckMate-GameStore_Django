"""Imported"""
from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """Class for products form"""

    class Meta:
        """Gets all fields except avgRating"""
        model = Product
        fields = '__all__'
        exclude = ('avgRating',) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


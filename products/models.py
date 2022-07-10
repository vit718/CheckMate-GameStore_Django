""" Imported"""
from django.db import models


class Category(models.Model):
    """
    A Class for the Products Categories
    """
    class Meta:
        """ Creates a Friendly name """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    A model for storing Product information
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    min_players = models.PositiveSmallIntegerField(null=True, blank=True)
    max_players = models.PositiveSmallIntegerField(null=True, blank=True)
    min_age = models.PositiveSmallIntegerField(null=True, blank=True)
    avgRating = models.FloatField(default=0,)
    play_time = models.PositiveSmallIntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    onSale = models.BooleanField(default=False)

    def price_onsale(self):
        return self.price - ((self.price * 50) / 100)

    def __str__(self):
        return self.name

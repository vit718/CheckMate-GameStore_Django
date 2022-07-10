"""Imported"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from products.models import Product


class Review(models.Model):
    """A model for user reviews"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(5)]
        )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

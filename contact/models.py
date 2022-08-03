"""Imported"""
from django.db import models


class ContactMessage(models.Model):
    """Class for contact us model"""
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "-" + self.email

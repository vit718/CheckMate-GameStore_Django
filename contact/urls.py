"""Imported"""
from django.urls import path
from .import views

urlpatterns = [
    path('', views.contactmessage, name='contactmessage'),
]

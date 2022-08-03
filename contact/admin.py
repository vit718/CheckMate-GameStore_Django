"""Imported"""
from django.contrib import admin
from .models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    """Class for admin contact messages"""
    list_display = ('name', 'email', 'subject', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'


admin.site.register(ContactMessage, ContactMessageAdmin)

"""Imported"""
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """Admin products"""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    list_filter = ('category',)

    ordering = ('sku',)

    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """Admin Category"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

"""Imported"""
from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """Calc the subtotal"""
    return price * quantity

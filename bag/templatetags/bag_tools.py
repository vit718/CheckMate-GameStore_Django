from django import template

register = template.Library()


@register.filter(name='calc_subtotal_onsale')
def calc_subtotal_onsale(price, quantity):
    return (round(price) * quantity)


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return (price * quantity)

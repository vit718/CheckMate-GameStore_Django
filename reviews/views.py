"""Imported"""
from django.shortcuts import render, get_object_or_404
from .models import Product, Review


def product_reviews(request, product_id):
    """ Display products reviews page """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id).order_by('-created_at')

    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'reviews/product_reviews.html', context)

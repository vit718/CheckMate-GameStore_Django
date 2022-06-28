# Imported models
from django.shortcuts import render, get_object_or_404
from. models import Product


def all_products(request):
    """ Display all products including search and filtering queries """

    products = Product.objects.order_by("name")

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Display products detail page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

from django.shortcuts import render
from. models import Product

def all_products(request):
    """ Display all products including search and filtering queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

"""Imported"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Avg
from .models import Product, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required



def product_reviews(request, product_id):
    """ Display products reviews page """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id).order_by('-created_at')

    average = reviews.aggregate(Avg("rating"))["rating__avg"]
    context = {
        'average': average,
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'reviews/product_reviews.html', context)



def reviews_form(request, product_id):
    """display reviews form"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'reviews/reviews_form.html', context)



@login_required
def add_review(request, product_id):
    """Add a new product review"""
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.comment = request.POST['comment']
            data.rating = request.POST['rating']
            data.user = request.user
            data.product = product
            data.save()
            return redirect(reverse('product_reviews', args=[product.id]))
        else:
            form = ReviewForm()
        return redirect(reverse('reviews_form', args=[product.id]))
    else:
        return redirect('accounts:login')

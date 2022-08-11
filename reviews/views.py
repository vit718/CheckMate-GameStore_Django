"""Imported"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from .models import Product, Review
from .forms import ReviewForm


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
            messages.success(
                request, f'You Added a new review for {product.name}'
                )
            return redirect(reverse('product_reviews', args=[product.id]))
        else:
            form = ReviewForm()
        return redirect(reverse('reviews_form', args=[product.id]))
    else:
        return redirect('accounts:login')


@login_required
def edit_review(request, product_id, review_id):
    """Edit a product review"""
    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(
        Review, product=product, id=review_id, user=request.user
        )
    form = ReviewForm(instance=review)
    context = {
        'form': form,
        'product': product,
        'review': review,
    }

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(
                request, f'You edited your review for {product.name}'
                )
            return redirect(reverse(product_reviews, args=[product.id]))
        else:
            messages.error(
                request, 'Please ensure your rating is between 0 and 5'
                )
            return render(request, 'reviews/edit_review.html', context)
    else:
        return render(request, 'reviews/edit_review.html', context)


@login_required
def delete_review(request, product_id, review_id):
    """Remove a product review"""
    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(
        Review, product=product, id=review_id, user=request.user
        )
    context = {
        'product': product,
        'review': review,
    }
    if request.method == "POST":
        review.delete()
        messages.success(
            request, f'You deleted a review for {product.name}'
        )
        return redirect(reverse('product_reviews', args=[product.id]))
    else:
        return render(request, 'reviews/delete_review.html', context)

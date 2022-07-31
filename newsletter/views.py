"""Imported"""
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber
from .forms import SubscriberForm


def newsletter(request):
    """A view to handle newsletter signup"""

    form = SubscriberForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Subscriber.objects.filter(email=instance.email).exists():
            messages.error(
                request,
                f"Sorry, {instance.email} already exists in our database.\
                           Please try again."
            )
            return redirect("home")
        else:
            instance.save()
            messages.success(
                request,
                f"Congratulations! {instance.email} \
                has been added to our mailing list."
            )
            return redirect("home")
    else:
        messages.error(
            request,
            "Please enter a valid email address."
        )
        return redirect("home")


def unsubscribe(request):
    """A view to handle unsubcribing users"""
    form = SubscriberForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Subscriber.objects.filter(email=instance.email).exists():
            Subscriber.objects.filter(email=instance.email).delete()
            messages.success(
                request,
                f"{instance.email} has been removed from our mailing list.",
            )
            return redirect("home")
        else:
            messages.error(
                request,
                f"Sorry, {instance.email} cannot be found in our database.\
                           Please try again.",
            )

    template = "newsletter/unsubscribe.html"
    context = {
        "form": form,
    }
    return render(request, template, context)

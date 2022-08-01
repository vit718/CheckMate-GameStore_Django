"""Imported"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
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
            # Send a confirmation email when email is added to the database
            cust_email = instance.email
            subject = render_to_string(
                'newsletter/confirmation_emails/ \
                confirmation_email_subject.txt',
                )
            body = render_to_string(
                'newsletter/confirmation_emails/confirmation_email_body.txt',
                {'contact_email': settings.DEFAULT_FROM_EMAIL})
            print(settings.DEFAULT_FROM_EMAIL)
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
                )

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
            # Send a confirmation email when email is deleted from the database
            cust_email = instance.email
            subject = render_to_string(
                'newsletter/confirmation_emails/ \
                unsubscribe_email_subject.txt',
                )
            body = render_to_string(
                'newsletter/confirmation_emails/unsubscribe_email_body.txt',
                {'contact_email': settings.DEFAULT_FROM_EMAIL})
            print(settings.DEFAULT_FROM_EMAIL)
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
                )
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

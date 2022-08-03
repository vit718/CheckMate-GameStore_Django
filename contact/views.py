""" Imported """
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm


def contactmessage(request):
    """Handles contact us submission"""
    form = ContactMessageForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Submitted')
            return redirect('contactmessage')
    else:
        context = {
            'form': form
        }
        return render(request, 'contact/contact_us.html', context)

""" Imported """
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm


def contactmessage(request):
    """Handles contact us submission"""
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, messages.INFO, 'Message Submitted.')
            return redirect('contactmessage')
    else:
        form = ContactMessageForm(request.POST or None)
    return render(request, 'contac/contact_us.html', {'form': form})

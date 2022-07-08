"""Imported"""
from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def profile(request):
    """ Display the user's profile. """
    myprofile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': myprofile,
    }

    return render(request, template, context)

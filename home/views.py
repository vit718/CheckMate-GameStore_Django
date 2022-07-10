from django.shortcuts import render
from newsletter.forms import SubscriberForm


def index(request):
    """ A view to return the index page """
    
    sub_form = SubscriberForm()

    context = {
        "sub_form": sub_form,
    }

    return render(request, 'home/index.html', context)

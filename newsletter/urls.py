from django.urls import path
from .import views

urlpatterns = [
    path("subscribed/", views.newsletter, name="newsletter"),
    path("unsubscribe/", views.unsubscribe, name="unsubscribe"),
]

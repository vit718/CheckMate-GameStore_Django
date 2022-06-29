from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('on_sale', views.on_sale, name='on_sale'),
    path('<product_id>', views.product_detail, name='product_detail'),
]

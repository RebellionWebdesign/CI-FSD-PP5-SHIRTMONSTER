from django.contrib import admin
from django.urls import path
from .views import ProductDetailView
from . import views



urlpatterns = [
    path('show_product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('add_to_list/<int:pk>', views.add_to_wishlist, name='add_to_wishlist'),
]
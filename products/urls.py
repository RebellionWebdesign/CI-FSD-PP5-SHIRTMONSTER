from django.contrib import admin
from django.urls import path
from .views import ProductDetailView


urlpatterns = [
    path('show_product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]
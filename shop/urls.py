from django.contrib import admin
from django.urls import path
from .views import ProductsShopView


urlpatterns = [
    path('shop/', ProductsShopView.as_view(), name='shop'),
]
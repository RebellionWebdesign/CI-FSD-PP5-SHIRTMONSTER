from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='cart'),
    path('add/<item_id>', views.add_to_cart, name='add_to_cart'),
    path('remove/<item_id>', views.adjust_cart_quantity, name='adjust_cart_quantity'),
]

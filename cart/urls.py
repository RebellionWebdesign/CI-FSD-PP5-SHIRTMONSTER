from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='cart'),
    path('add/<item_id>', views.add_to_cart, name='add_to_cart'),
    path('update/<item_id>', views.adjust_cart_quantity,
         name='update_cart_quantity'),
    path('remove/<item_id>', views.remove_from_cart, name='remove_from_cart'),
]

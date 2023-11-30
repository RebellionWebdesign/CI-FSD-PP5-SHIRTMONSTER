from django.shortcuts import render
from django.views import View

def view_cart(request):
    """
    A view which lets shoppers view the shopping cart
    """
    return render(request, 'cart/cart.html')

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from users.models import UserAdress
from .forms import OrderForm
from cart.contexts import cart_contents
import stripe

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'There is nothing in your bag!')
        return redirect(reverse('shop'))
    
    current_cart = cart_contents(request)
    total = current_cart["grand_total"]
    stripe_total = round(total*100)
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': settings.STRIPE_SECRET_KEY,
    }

    return render(request, template, context)

from django.shortcuts import render, redirect, reverse
from django.views import View

def view_cart(request):
    """
    A view which lets shoppers view the shopping cart
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a specified product to the shopping cart """

    quantity = int(request.POST.get('quantity-counter'))

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
    
    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart_quantity(request, item_id):
    """ Remove a specified product from the shopping cart """

    quantity = int(request.POST.get('quantity-counter'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop[item_id]

    request.session['cart'] = cart
    return redirect(reverse('cart'))

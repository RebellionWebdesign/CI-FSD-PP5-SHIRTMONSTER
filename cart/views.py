from django.shortcuts import render, redirect
from django.views import View

def view_cart(request):
    """
    A view which lets shoppers view the shopping cart
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a specified product to the shopping cart """

    quantity = 0

    if quantity < 1:
        quantity = 1
    else:
        quantity = int(request.POST.get('quantity'))

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)

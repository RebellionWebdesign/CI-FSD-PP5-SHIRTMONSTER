from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product

def view_cart(request):
    """ A view which lets shoppers view the shopping cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a specified product to the shopping cart """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity-counter'))

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.add_message(request, messages.SUCCESS, "Product added!")
    else:
        cart[item_id] = quantity
        messages.add_message(request, messages.SUCCESS, "Product added!")
    
    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart_quantity(request, item_id):
    """ Change the item quantity in the cart, or enter "0" to delete """

    quantity = int(request.POST.get('quantity-counter'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('cart'))


def remove_from_cart(request, item_id):
    """ Remove a specified product from the shopping cart """

    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
    
#def cart_to_order(request, item_id):
    #do stuff

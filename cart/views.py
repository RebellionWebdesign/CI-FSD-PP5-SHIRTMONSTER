from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ A view which lets shoppers view the shopping cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a specified product to the shopping cart """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity-counter', 1))

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    current_cart_items = cart.get(item_id, 0)

    if item_id in list(cart.keys()):
        if current_cart_items + quantity > 5:
            (messages.error(request, 'You only can have 5 items of each!'))
            quantity = 5 - current_cart_items
        else:
            cart[item_id] += quantity
            messages.add_message(request, messages.SUCCESS, "Product added!")
            print(current_cart_items)
            print(quantity)
    else:
        cart[item_id] = quantity
        messages.add_message(request, messages.SUCCESS, "Product added!")

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart_quantity(request, item_id):
    """ Change the item quantity in the cart, or enter "0" to delete """

    quantity = int(request.POST.get('quantity-counter'))
    cart = request.session.get('cart', {})

    if quantity > 5:
        messages.error(request, 'You only can have 5 items of each!')
        quantity = 5
    else:
        pass

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

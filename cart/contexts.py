from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    tax = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        tax = total * Decimal(settings.TAX_PERCENTAGE)
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'total': total,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        shipping = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        free_delivery_amount_left = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        shipping = 0
        free_delivery_amount_left = 0

    grand_total = shipping + total + tax

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'free_delivery_amount_left': free_delivery_amount_left,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'tax': tax,
    }

    return context

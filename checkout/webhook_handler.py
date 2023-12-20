from django.http import HttpResponse
import stripe
from .models import Order, OrderItem
from products.models import Product
import json
import time


class StripeWH_Handler:
    """ handles Stripe webhooks """

    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        """ Handles unexpected/generic webhook events """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
            )

    def handle_payment_intent_succeeded(self, event):
        """ Handles the payment succeded webhook """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean Shipping details data
        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    zip_code=shipping_details.address.zip_code,
                    city__iexact=shipping_details.address.city,
                    adress_line_1__iexact=shipping_details.address_line_1,
                    adress_line_2__iexact=shipping_details.address_line_2,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone=shipping_details.phone,
                    country=shipping_details.address.country,
                    zip_code=shipping_details.address.zip_code,
                    city=shipping_details.address.city,
                    adress_line_1=shipping_details.adress_line_1,
                    adress_line_2=shipping_details.adress_line_2,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handles the payment failed webhook """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
            )




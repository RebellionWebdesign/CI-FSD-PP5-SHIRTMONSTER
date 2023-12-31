from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.views import View
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderItem
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from products.models import Product
from cart.contexts import cart_contents
import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Payment Error. Please try later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    user_profile_id = None
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            user_profile_id = profile.id
        except UserProfile.DoesNotExist:
            messages.error(
                "Sorry, there was a problem with your profile."
                "Please contact us.")

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if request.user.is_authenticated:
            form_data = {
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'phone': request.POST['phone'],
                'country': request.POST['country'],
                'zip_code': request.POST['zip_code'],
                'city': request.POST['city'],
                'adress_line_1': request.POST['adress_line_1'],
                'adress_line_2': request.POST['adress_line_2'],
                'user_profile': int(user_profile_id),
            }
        else:
            form_data = {
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'phone': request.POST['phone'],
                'country': request.POST['country'],
                'zip_code': request.POST['zip_code'],
                'city': request.POST['city'],
                'adress_line_1': request.POST['adress_line_1'],
                'adress_line_2': request.POST['adress_line_2'],
            }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found"
                        "in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form.'
                           'Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request, "There's nothing in your cart at the moment")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone': profile.phone,
                    'country': profile.country,
                    'zip_code': profile.zip_code,
                    'city': profile.city,
                    'adress_line_1': profile.adress_line_1,
                    'adress_line_2': profile.adress_line_2,
                    'user_profile': user_profile_id,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm(initial={
                    'user_profile': user_profile_id,
                })
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        order.user_profile = profile
        order.save()

    if save_info:
        profile_data = {
            'phone': order.phone,
            'zip_code': order.zip_code,
            'city': order.city,
            'adress_line_1': order.adress_line_1,
            'adress_line_2': order.adress_line_2,
            'country': order.country,
        }

        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

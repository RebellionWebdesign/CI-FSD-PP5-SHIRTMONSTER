from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib.auth.models import User
from checkout.models import Order
from .models import UserProfile
from testimonial.models import Testimonial
from testimonial.forms import TestimonialForm
from . import forms

class UserProfileView(LoginRequiredMixin, View):
    template_name = 'profiles/profiles.html'
    context_object_name = 'profile'

    def get(self, request, pk):

        user = get_object_or_404(User, pk=pk)
        profile, created = UserProfile.objects.get_or_create(user=user)
        if not hasattr(user, 'userprofile'):
            user.userprofile = profile
        orders = Order.objects.filter(user_profile=profile)
        form = forms.UserProfileForm(instance=profile)
        form.set_update_user(user)
        context = {
            'user': user,
            'form': form,
            'orders': orders,
        }

        return render(request, 'profiles/profiles.html', context)
    
    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        profile = request.user.userprofile
        form = forms.UserProfileForm(request.POST, instance=user.userprofile)
        form.set_update_user(user)
        context = {
            'user': user,
            'form': form,
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
        else:
            messages.error(request, 'Whoops! Something went wrong while saving your data. Please check the form again!')
        
        return render(request, 'profiles/profiles.html', context)

    def get_object(self):
        return self.request.user

class OrderOverview(LoginRequiredMixin, View):
    """
    This view provides the testimonial field and an order overview
    for registered customers
    """
    def get(self, request, order_number):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        orders = get_object_or_404(Order, user_profile=user_profile, order_number=order_number)
        testimonial_form = TestimonialForm()
        testimonial_form.set_content(order_number)
        testimonial_content = Testimonial.objects.filter(user_id=request.user, order_id=orders)
        order_items = orders.order_items.all()
        context = {
            'orders': orders,
            'order_items': order_items,
            'testimonial_form': testimonial_form,
            'testimonial_content': testimonial_content
        }

        return render(request, 'profiles/order_detail.html', context)


    def post(self, request, order_number):
        order = get_object_or_404(Order, order_number=order_number)
        testimonial, created = Testimonial.objects.get_or_create(user_id=request.user, order_id=order)

        testimonial_form = TestimonialForm(data=request.POST, instance=testimonial)
        if testimonial_form.is_valid():
            testimonial_form.save()
            messages.success(request, 'Thanks for your testimonial!')
        else:
            messages.error(request, 'Ooops...something went wrong here. Please check your testimonial.')

        return redirect(reverse('order_detail', kwargs={'order_number': order_number}))

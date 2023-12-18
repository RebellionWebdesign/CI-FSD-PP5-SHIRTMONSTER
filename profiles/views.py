from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib.auth.models import User
from checkout.models import Order
from .models import UserProfile
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
        profile, created = UserProfile.objects.get_or_create(user=user)
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

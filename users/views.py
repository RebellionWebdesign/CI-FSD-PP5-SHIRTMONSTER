from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import User

class UserProfileView(LoginRequiredMixin, View):
    template_name = 'users/user_profile.html'
    context_object_name = 'user_profile'

    def get(self, request, pk):

        users = User.objects.filter(pk=pk)
        context = {
            "users": users,
        }

        return render(request, 'users/user_profile.html', context)
    
    def get_object(self):
        return self.request.user

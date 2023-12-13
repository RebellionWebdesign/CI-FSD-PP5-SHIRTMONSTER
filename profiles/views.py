from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib.auth.models import User

class UserProfileView(LoginRequiredMixin, View):
    template_name = 'profiles/profiles.html'
    context_object_name = 'profile'

    def get(self, request, pk):

        users = User.objects.filter(pk=pk)
        context = {
            "users": users,
        }

        return render(request, 'profiles/profiles.html', context)
    
    def get_object(self):
        return self.request.user

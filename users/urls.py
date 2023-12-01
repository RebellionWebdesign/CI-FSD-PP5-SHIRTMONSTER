from django.contrib import admin
from django.urls import path
from .views import UserProfileView


urlpatterns = [
    path('show_user/<int:pk>', UserProfileView.as_view(), name='user_profile'),
]

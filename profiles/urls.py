from django.contrib import admin
from .views import UserProfileView
from django.urls import path

urlpatterns = [
    path('show_user/<int:pk>', UserProfileView.as_view() , name='profile')
]
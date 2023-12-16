from django.contrib import admin
from .views import UserProfileView, OrderHistory
from django.urls import path

urlpatterns = [
    path('show_user/<int:pk>', UserProfileView.as_view() , name='profile'),
    path('order_history/<order_number>', OrderHistory.as_view() , name='order_history'),
]
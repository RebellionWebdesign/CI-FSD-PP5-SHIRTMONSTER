from django.contrib import admin
from .views import UserProfileView, OrderOverview
from django.urls import path

urlpatterns = [
    path('show_user/<int:pk>', UserProfileView.as_view() , name='profile'),
    path('order_detail/<str:order_number>', OrderOverview.as_view() , name='order_detail'),
]
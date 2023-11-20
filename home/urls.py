from django.contrib import admin
from django.urls import path
from . import views
from products.views import ProductsHomeView

urlpatterns = [
    path('', views.home, name='home'),
    path('', ProductsHomeView.as_view(), name='all_products'),
]

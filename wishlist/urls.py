from django.urls import path
from .views import WishView


urlpatterns = [
    path('wishlist/', WishView.as_view(), name='user_wishlist'),
]
from django.urls import path
from wishlist.models import WishList
from .views import WishView, RemoveWish


urlpatterns = [
    path('wishlist/', WishView.as_view(), name='user_wishlist'),
    path('remove_from_list/<int:pk>', RemoveWish.as_view(), name='remove_from_wishlist'),
]
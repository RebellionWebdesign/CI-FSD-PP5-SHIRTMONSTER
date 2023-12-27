from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product
from .models import WishList
from django.contrib import messages


class WishView(LoginRequiredMixin, View):
    """ This displays the users wishlist on the wishlist page """

    def get(self, request):
        user = request.user
        wishes = WishList.objects.filter(user_id=user)
        context = {
            "wishes": wishes,
        }

        return render(request, 'wishlist/wishlist.html', context)


class RemoveWish(LoginRequiredMixin, View):
    """ Deletes an item from the wishlist """

    def post(self, request, pk):
        wish_product = get_object_or_404(Product, pk=pk)
        wish_item = WishList.objects.filter(product_id=wish_product)

        wish_item.delete()
        messages.success(request, 'Product removed from wishlist!')

        return redirect(reverse('user_wishlist'))

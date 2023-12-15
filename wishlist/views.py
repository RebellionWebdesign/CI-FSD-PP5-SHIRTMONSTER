from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from products.models import Product
from .models import WishList
from django.contrib import messages

class WishView(View):
    """ This displays the users wishlist on the wishlist page """

    def get(self, request):
        wishes = WishList.objects.all()
        context = {
            "wishes": wishes,
        }
    
        return render(request, 'wishlist/wishlist.html', context)


class RemoveWish(View):
    """ Deletes an item from the wishlist """

    def post(self, request, pk):
        wish_product = get_object_or_404(Product, pk=pk)
        wish_item = WishList.objects.filter(product_id=wish_product)

        wish_item.delete()
        messages.success(request, 'Product removed from wishlist!')
    
        return redirect(reverse('user_wishlist'))

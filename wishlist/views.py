from django.shortcuts import render
from django.views import View
from .models import WishList

class WishView(View):
    """ This displays the users wishlist on the wishlist page """

    def get(self, request):
        wishes = WishList.objects.all()
        context = {
            "wishes": wishes,
        }
    
        return render(request, 'wishlist/wishlist.html', context)

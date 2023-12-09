from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class WishList(models.Model):
    """ this model stores the users wish list """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist_user")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlist_product")
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str("Wishlist")
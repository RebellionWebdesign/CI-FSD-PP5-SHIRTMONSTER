from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from .models import Product, ProductCategory
from django.contrib import messages
from products.models import Product
from wishlist.models import WishList

class ProductsHomeView(View):
    """
    A view which gets all products from the database, so they can be
    displayed on the homepage
    """
    def get_products(request):

        products = Product.objects.all()
        categories = ProductCategory.objects.all()
        context = {
            "products": products,
            "categories": categories,
        }

        return render(request, 'home/index.html', context)

class ProductDetailView(View):
    """
    A view to show the detail page for a given product
    """
    def get(self, request, pk):

        products = Product.objects.filter(pk=pk)
        categories = ProductCategory.objects.all()
        context = {
            "products": products,
            "categories": categories,
        }

        return render(request, 'products/product_detail.html', context)

def add_to_wishlist(request, pk):
    """ A view to let users add products to a wishlist """

    user = request.user
    product = get_object_or_404(Product, pk=pk)
    wishlist_item = WishList.objects.filter(user_id=user, product_id=product)

    if wishlist_item.exists():
        messages.info(request, "Item is already in wishlist.")
        pass
    else:
        wish = WishList()
        wish.user_id = user
        wish.product_id = product
        wish.full_clean()
        wish.save()
        messages.success(request, 'Product added to wishlist!')
    
    return redirect(reverse('product_detail', kwargs={'pk': product.pk}))


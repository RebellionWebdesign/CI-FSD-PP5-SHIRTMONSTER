from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from .models import Product, ProductCategory

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

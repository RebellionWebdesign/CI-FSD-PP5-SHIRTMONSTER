from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product

class ProductsHomeView(View):

    def get_products(request):

        products = Product.objects.all()
        context = {
            "products": products
        }

        return render(request, 'home/index.html', context)


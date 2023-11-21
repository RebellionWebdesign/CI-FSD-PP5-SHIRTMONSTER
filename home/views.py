from django.shortcuts import render
from django.views import View
from products.models import Product, ProductCategory

class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        categories = ProductCategory.objects.all()
        context = {
            "products": products,
            "categories": categories,
        }
    
        return render(request, 'home/index.html', context)

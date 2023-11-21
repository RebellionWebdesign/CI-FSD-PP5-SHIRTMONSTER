from django.shortcuts import render
from django.views import View
from products.models import Product

class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            "products": products
        }
    
        return render(request, 'home/index.html', context)

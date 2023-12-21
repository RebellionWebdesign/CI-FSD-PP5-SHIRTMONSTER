from django.shortcuts import render
from django.views import View
from products.models import Product, ProductCategory
from testimonial.models import Testimonial

class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        categories = ProductCategory.objects.all()
        testimonials = Testimonial.objects.all()
        context = {
            "products": products,
            "categories": categories,
            "testimonials": testimonials,
        }
    
        return render(request, 'home/index.html', context)

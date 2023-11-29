from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.views import View
from products.models import Product, ProductCategory

class ProductsShopView(View):
    """
    A view which lets the user search for products on the shop page,
    includes filtering and searching products
    """
    def get(self, request):

        products = Product.objects.all()
        categories = ProductCategory.objects.all()
        query = None
        category = None

        if request.GET:

            if 'category' in request.GET:
                categories = request.GET['category'].split(',')
                products = products.filter(category_id__name__in=categories)
                categories = ProductCategory.objects.filter(name__in=categories)

            if 'main-search' in request.GET:
                query = request.GET['main-search']
                if not query:
                    messages.error(request, "Please fill in the search form!")
                    return redirect(reverse('products'))
                
                queries = Q(name__icontains=query) | Q(description__icontains=query)
                products = products.filter(queries)
        
        context = {
            "products": products,
            "categories": categories,
            "search_term": query,
            "currents_categories": categories,
        }

        return render(request, 'shop/shop.html', context)

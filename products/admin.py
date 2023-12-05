from django.contrib import admin
from .models import Product, ProductCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sizes',
        'ean',
        'category_id',
        'price',
        'rating',
        'image',
        'created_at',
        'modified_at',
    )

    ordering = ('ean',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
        'description',
        'created_at',
        'modified_at',
    )




admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, CategoryAdmin)

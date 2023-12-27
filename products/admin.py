from django.contrib import admin
from .models import Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'ean',
        'category_id',
        'price',
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

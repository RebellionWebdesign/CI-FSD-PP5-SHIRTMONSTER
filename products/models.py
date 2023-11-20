from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=128)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_display_name(self):
        return self.display_name


class ProductInventory(models.Model):
    quantity = models.IntegerField()


class Product(models.Model):
    image_url = models.URLField()
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=128)
    ean = models.CharField(max_length=13)
    category_id = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.SET_NULL)
    inventory_id = models.ForeignKey(ProductInventory, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.FloatField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


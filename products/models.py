from django.db import models

class ProductCategory(models.Model):
    """This model holds the category data, e.g shirts, hoodies etc."""
    name = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=128)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    ordering = ['-date']

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name
    
    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    """This model holds the product data"""

    image_url = models.URLField()
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=254)
    ean = models.CharField(max_length=13)
    category_id = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.SET_NULL)
    quantity= models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


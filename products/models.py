from django.db import models

class Product(models.Model):
    #image = DECIDE ON RELATION 
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=128)
    ean = models.CharField(max_length=13)
    #category_id = DECIDE ON RELATION
    #inventory_id = DECIDE ON RELATION
    price = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)



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
    #category_id = DECIDE ON RELATION

#from django.db import models
#from django.contrib.auth.models import User
#from products.models import Product
#from users.models import UserAdress


#class Order(models.Model):
#    order_number = models.CharField()
#    user_id = models.ForeignKey(User)
#    primary_address_id = models.OneToOneField(UserAdress)
#    secondary_address_id = models.OneToOneField(UserAdress)
#    product_id = models.ForeignKey(Product)
#    order_date = models.DateTimeField
#    order_cost = models.DecimalField()
#    tax_amount = models.DecimalField()
#    delivery_cost = models.DecimalField()
#    order_total = models.DecimalField()
#    order_status = models.IntegerField()
#    payment = models.IntegerField()
#    shipping_status = models.IntegerField()


#class CancelledOrders(models.Model):
#    order_number = models.OneToOneField(Order)
#    user_id = models.ForeignKey(User)
#    requested_on = models.DateField()
#    cancel_reason = models.IntegerField()
#    other_reason = models.TextField()
#    cancel_status = models.IntegerField()
#    resolved_on = models.DateField()
#    resolved_by = models.IntegerField()

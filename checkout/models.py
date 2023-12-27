import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product
from django_countries.fields import CountryField
from profiles.models import UserProfile
from django.contrib import messages


class Order(models.Model):
    """ This class handles the orders """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name="order_profile")
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    adress_line_1 = models.CharField(max_length=160, null=False, blank=False)
    adress_line_2 = models.CharField(max_length=160, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """ Generates an order number as uuid """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Updates grand total and delivery cost for each new order item """
        order_items = self.order_items.all()
        self.order_total = order_items.aggregate(Sum('orderitem_total'))[
            'orderitem_total__sum'] or 0
        print(self.order_total)

        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.shipping_cost = self.order_total * \
                settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.shipping_cost = 0
        self.grand_total = self.order_total + self.shipping_cost
        self.save()

    def save(self, *args, **kwargs):
        """ Override the default save method if there isnt an order number """
        if not self.order_number:
            self.order_number = self._generate_order_number()
            super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='order_items')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    orderitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False,
        editable=False)

    def save(self, *args, **kwargs):
        """
        Override the default save method to set the order item
        total and update order total
        """
        self.orderitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'EAN {self.product.ean} on order {self.order.order_number}'

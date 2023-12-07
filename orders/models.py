from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from users.models import UserAdress


class Order(models.Model):
    """ This model handles the orders """

    PENDING = 'Pending'
    PROCESSING = 'Processing'
    SHIPPED = 'Shipped'
    COMPLETED = 'Completed'
    REFUNDED = 'Refunded'

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (SHIPPED, 'Shipped'),
        (COMPLETED, 'Completed'),
        (REFUNDED, 'Refunded'),
    )

    PAYMENT_CHOICES = (
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed')
    )

    SHIPPING_CHOICES = (
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (SHIPPED, 'Shipped'),
    )

    order_number = models.CharField(max_length=7, null=False, editable=False)
    user_id = models.OneToOneField(User, on_delete=models.PROTECT, related_name="user_id")
    address_id = models.OneToOneField(UserAdress, on_delete=models.CASCADE, related_name="user_address")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_id")
    order_date = models.DateField(auto_now_add=True)
    order_cost = models.DecimalField(max_digits=6, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=6, decimal_places=2)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2)
    order_total = models.DecimalField(max_digits=6, decimal_places=2)
    order_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default=PENDING)
    shipping_status = models.CharField(max_length=10,choices=SHIPPING_CHOICES, default=PENDING)

    class Meta:
        """ Ordering rule for orders """
        ordering = ('-order_date',)
    
    def __str__(self):
        """ Display class name as order number """
        return self.order_number


class CancelledOrders(models.Model):
    """ This model displays cancellation request data"""

    PENDING = 'Pending'
    PROCESSING = 'Processing'
    GRANTED = 'Granted'
    DECLINED = 'Declined'

    CANCEL_CHOICES = (
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (GRANTED, 'Granted'),
        (DECLINED, 'Declined'),
    )

    DEFAULT = 'Choose...'
    DEFECTIVE = 'Defective'
    ORDERED_WRONG = 'Ordered wrong item'
    UNAUTHORIZED_PURCHASE = 'Unauthorized Purchase'
    SIMPLE_RETURN = 'Just return'

    CANCEL_REASONS = (
        (DEFAULT, 'Choose...'),
        (DEFECTIVE, 'Defective'),
        (ORDERED_WRONG, 'Ordered wrong item'),
        (UNAUTHORIZED_PURCHASE, 'Unauthorized purchase'),
        (SIMPLE_RETURN, 'Just return'),
    )

    order_number = models.OneToOneField(Order, on_delete=models.PROTECT, related_name="order_id")
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="order_user")
    requested_on = models.DateField(auto_now_add=True)
    cancel_reason = models.CharField(max_length=30,choices=CANCEL_REASONS, default=DEFAULT)
    other_reason = models.TextField()
    cancel_status = models.CharField(max_length=10,choices=CANCEL_CHOICES, default=PENDING)
    resolved_on = models.DateField(auto_now_add=True)
    resolved_by = models.OneToOneField(User, on_delete=models.PROTECT, related_name="cancel_user")

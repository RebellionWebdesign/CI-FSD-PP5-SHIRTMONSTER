from django.db import models
from django.contrib.auth.models import User
from checkout.models import Order

class Testimonial(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id
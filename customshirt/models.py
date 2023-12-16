from django.db import models

class CustomShirt(models.Model):
    """ This model saves inquiries for custom shirts """
    full_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    inquiry = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
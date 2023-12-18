from django.db import models

class CustomShirt(models.Model):
    """ This model saves inquiries for custom shirts """
    full_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    inquiry = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='custom_shirts', null=False, blank=False)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
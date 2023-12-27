from django.db import models
from django.utils.html import mark_safe


class CustomShirt(models.Model):
    """ This model saves inquiries for custom shirts """
    full_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    inquiry = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='custom_shirts', null=True, blank=True)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    def image_tag(self):
        return mark_safe('<img src="https://shirtmonster.s3.eu-central-'
                         '1.amazonaws.com/%s"'
                         'width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    """
    This model acts as an extension to the default User model, providing extra
    fields for a user image.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    user_image = models.ImageField(blank= True, null= True)
    user_image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class UserAdress(models.Model):
    """
    This model stores the shipping data for a user.
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_address")
    adress_line_1 = models.CharField(max_length=35)
    adress_line_2 = models.CharField(blank=True, null=True, max_length=35)
    city = models.CharField(max_length=35)
    zip_code = models.CharField(max_length=35)
    country = models.CharField(max_length=35)
    telephone = models.CharField(blank=True, null=True, max_length=35)
    mobile_phone = models.CharField(blank=True, null=True, max_length=35)

    class Meta:
        verbose_name_plural = 'User addresses'
    
    def __str__(self):
        return self.user_id


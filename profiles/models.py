from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

class UserProfile(models.Model):
    """
    This model stores the user profiles and their data.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    adress_line_1 = models.CharField(max_length=80, null=False, blank=False)
    adress_line_2 = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=UserProfile)
def create_or_update_profile(sender, instance, created, **kwargs):
    """ Creates or saves the user profile """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

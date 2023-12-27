from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import UserProfile
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """ Creates or saves the user profile """
    if created:
        profile, profile_created = UserProfile.objects.get_or_create(
            user=instance)
        if profile_created:
            instance.userprofile = profile
            instance.save()
        else:
            profile.save()

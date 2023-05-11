from django.db.models.signals import post_save
from django.dispatch import receiver

from WISDjango import settings
from app.models import Profile, CustomUser


@receiver(post_save, sender=CustomUser)
def profile_create_signal(sender, instance=None, created=None, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()

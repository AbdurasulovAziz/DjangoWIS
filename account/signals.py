from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model

from account.models import Profile


@receiver(post_save, sender=get_user_model())
def profile_create_signal(sender, instance=None, created=None, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()

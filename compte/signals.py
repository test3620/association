# Importation de modules.
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

from .models import Membre

@receiver(post_save, sender=Membre)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(membre=instance)

@receiver(post_save, sender=Membre)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
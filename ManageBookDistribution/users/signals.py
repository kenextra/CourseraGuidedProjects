from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# This is a signal that gets fired after an object is saved
# The signal will be received by the receiver, which is the create_profile function
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
# This is a signal that gets fired after an object is saved
# The signal will be received by the receiver, which is the save_profile function
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
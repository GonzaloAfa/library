from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Workspace(models.Model):

    title = models.CharField(max_length=60)
    description = models.TextField()
    ref_user = models.ForeignKey(User,models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField(max_length=500, blank=True)
    last_name = models.TextField(max_length=500, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    workspace_active = models.TextField(max_length=60, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

        workspace = Workspace(
            title="Default",
            description="",
            ref_user=instance
        )
        workspace.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

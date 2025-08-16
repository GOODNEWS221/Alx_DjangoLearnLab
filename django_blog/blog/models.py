from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def profile_upload_to(instance, filename):
    return f"profiles/user_{instance.user.id}/{filename}"

class Post(models.Model):
    title = models.CharField(max_length=200)  # Blog post title
    content = models.TextField()  # Blog post content
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )  # Author linked to Django User
    published_date = models.DateTimeField(auto_now_add=True)  # Auto timestamp when created


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to=profile_upload_to, blank=True, null=True)

    def __str__(self):
        return f"Profile({self.user.username})"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

# Create your models here.

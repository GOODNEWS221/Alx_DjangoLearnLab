from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


def profile_upload_to(instance, filename):
    return f"profiles/user_{instance.user.id}/{filename}"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)  # Blog post title
    content = models.TextField()  # Blog post content
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    published_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("Tag", blank=True, related_name="posts")  # ✅ safe string ref

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to=profile_upload_to, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return f"Profile({self.user.username})"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # Show latest comments first

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"


# 🔔 Signals to auto-create Profile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

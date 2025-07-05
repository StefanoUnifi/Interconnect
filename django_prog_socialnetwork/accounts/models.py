from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    avatar = models.ImageField(upload_to='avatar', default='default_user.png', blank=False)
    bio = models.TextField(max_length=150, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

class UserFollowing(models.Model):
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='following'
    )
    following_user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='followers'
    )



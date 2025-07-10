import os
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    avatar = models.ImageField(upload_to='avatar', default='user_avatar.png', blank=False)
    bio = models.TextField(max_length=150, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        try:
            if self.avatar and hasattr(self.avatar, 'path') and os.path.isfile(self.avatar.path):
                image = Image.open(self.avatar.path)

                aspect_ratio = image.width / image.height
                if aspect_ratio > 1:
                    new_width = image.height
                    new_height = image.height
                else:
                    new_width = image.width
                    new_height = image.width

                left = (image.width - new_width) // 2
                top = (image.height - new_height) // 2
                right = left + new_width
                bottom = top + new_height

                cropped_image = image.crop((left, top, right, bottom))
                cropped_image = cropped_image.resize((600, 600), Image.ANTIALIAS)
                cropped_image.save(self.avatar.path)

        except Exception as e:
            print(f"Errore durante il salvataggio avatar: {e}")


class UserFollowing(models.Model):
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='following'
    )
    following_user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='followers'
    )
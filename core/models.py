import uuid
from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to="profile_images", default="wink.png")
    location = models.CharField(max_length=100, blank=True)

    # returning the username
    def __str__(self):
        return self.user.username


# model for post
class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    task = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user

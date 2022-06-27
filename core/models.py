import uuid
from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.


# model for post
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=180 , default="")
    task = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user

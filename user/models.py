from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    token = models.UUIDField(blank=True, null=True, unique=True)
    avatar = models.FileField(upload_to='avatars/', blank=True, null=True)
    avatar_url = models.URLField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

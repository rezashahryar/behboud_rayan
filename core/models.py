from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.


class User(AbstractUser):
    username = None
    mobile = models.CharField(max_length=11)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']

    objects = CustomUserManager()
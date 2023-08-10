from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string

from utils import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=20, verbose_name='страна', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    is_email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, **NULLABLE)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
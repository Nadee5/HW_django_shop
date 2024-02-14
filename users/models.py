import random

from django.contrib.auth.models import AbstractUser
from django.db import models

from shop.models import NULLABLE


class User(AbstractUser):
    username = None

    code = ''.join([str(random.randint(0, 9)) for _ in range(6)])

    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='номер телефона')
    country = models.CharField(max_length=100, **NULLABLE, verbose_name='страна')

    verify_code = models.CharField(max_length=6, default=code, verbose_name='Код верификации')
    is_verified = models.BooleanField(default=False, verbose_name='Верификация')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []



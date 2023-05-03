from django.db import models

from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from .manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=255)
    last_name = models.CharField('last_name', max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

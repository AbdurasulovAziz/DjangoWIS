from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.utils import timezone
from django.db import models

from .manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name')
    last_name = models.CharField('last_name')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField('Телефон', validators=[RegexValidator('[+]\d+$')])
    age = models.IntegerField('Возраст')
    region = models.CharField('Регион проживания пользователя')
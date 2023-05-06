import datetime
from datetime import timedelta

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.utils import timezone
from django.db import models

from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', blank=True)
    last_name = models.CharField('last_name', blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField('Phone', validators=[RegexValidator('[+]\d+$')], blank=True)
    birth_day = models.DateField('Birth day', blank=True, null=True)
    region = models.CharField('Region', blank=True)

    @property
    def age(self):
        result = datetime.date.today() - self.birth_day
        return result.days // 365

    def __str__(self):
        return self.user.email


class Dish(models.Model):
    name = models.CharField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Sause(Dish):

    def __str__(self):
        return self.name


class FoodMenu(Dish):
    TYPE_DISH = (
        ('Пицца', 'Пицца'),
        ('Суши', 'Суши'),
        ('Плов', 'Плов'),
        ('Шашлык', 'Шашлык'),
    )
    cook_time = models.IntegerField()
    category = models.CharField(choices=TYPE_DISH)
    sause = models.ForeignKey(Sause, on_delete=models.CASCADE)


class DrinkMenu(Dish):
    TYPE_DRINK = (
        ('Горячие напитки', 'Горячие напитки'),
        ('Холодные напитки', 'Холодные напитки'),
        ('Алкогольные напитки', 'Алкогольные напитки'),
    )
    category = models.CharField(choices=TYPE_DRINK)


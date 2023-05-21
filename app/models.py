from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from app.managers import NonAlcoholicDrinkManager


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

    objects = models.Manager()
    nonalco = NonAlcoholicDrinkManager()





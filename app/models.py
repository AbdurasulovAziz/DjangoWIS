from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class DishAbstractModel(models.Model):
    name = models.CharField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Sauce(DishAbstractModel):
    pass


class Dessert(DishAbstractModel):
    pass


class IceCream(DishAbstractModel):
    pass


class Food(DishAbstractModel):
    TYPE_DISH = (
        ('Burger', 'Burger'),
        ('Twister', 'Twister'),
        ('Bucket', 'Bucket'),
    )
    category = models.CharField(choices=TYPE_DISH)
    spicy = models.BooleanField(default=False)


class Drink(DishAbstractModel):
    TYPE_DRINK = (
        ('Cold', 'Cold Drinks'),
        ('Hot', 'Hot Drinks'),
        ('Milkshake', 'Milkshakes')
    )

    liter = models.FloatField()
    category = models.CharField(choices=TYPE_DRINK)



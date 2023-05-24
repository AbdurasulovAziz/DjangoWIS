from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

class PriceMixinFieldModel(models.Model):
    price = models.IntegerField(default=0)

    class Meta:
        abstract = True


class NameMixinFieldModel(models.Model):
    name = models.CharField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class OnStopMixinFieldModel(models.Model):
    on_stop = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Sauce(NameMixinFieldModel, PriceMixinFieldModel, OnStopMixinFieldModel):
    pass


class Dessert(NameMixinFieldModel, PriceMixinFieldModel, OnStopMixinFieldModel):
    pass


class Food(NameMixinFieldModel, PriceMixinFieldModel, OnStopMixinFieldModel):
    TYPE_DISH = (
        ('Burger', 'Burger'),
        ('Twister', 'Twister'),
        ('Bucket', 'Bucket'),
    )
    category = models.CharField(choices=TYPE_DISH)
    spicy = models.BooleanField(default=False)


class Drink(NameMixinFieldModel, PriceMixinFieldModel, OnStopMixinFieldModel):
    TYPE_DRINK = (
        ('Cold', 'Cold Drinks'),
        ('Hot', 'Hot Drinks'),
        ('Milkshake', 'Milkshakes')
    )

    liter = models.FloatField()
    category = models.CharField(choices=TYPE_DRINK)

    def __str__(self):
        return f'{self.name} {self.liter}'


class BoxMix(OnStopMixinFieldModel, NameMixinFieldModel):
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    drink = models.ForeignKey(Drink, on_delete=models.DO_NOTHING, blank=True)
    sauce = models.ForeignKey(Sauce, on_delete=models.DO_NOTHING, blank=True)
    dessert = models.ForeignKey(Dessert, on_delete=models.DO_NOTHING, blank=True)

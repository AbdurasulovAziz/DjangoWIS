from django.contrib.auth import get_user_model
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class Dish(models.Model):
    name = models.CharField()
    price = models.IntegerField(default=0)
    on_stop = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Sauce(Dish):
    pass


class Dessert(Dish):
    pass


class Food(Dish):
    TYPE_DISH = (
        ("Burger", "Burger"),
        ("Twister", "Twister"),
        ("Bucket", "Bucket"),
    )
    category = models.CharField(choices=TYPE_DISH)
    spicy = models.BooleanField(default=False)


class Drink(Dish):
    TYPE_DRINK = (
        ("Cold", "Cold Drinks"),
        ("Hot", "Hot Drinks"),
        ("Milkshake", "Milkshakes"),
    )

    liter = models.FloatField()
    category = models.CharField(choices=TYPE_DRINK)

    def __str__(self):
        return f"{self.name} {self.liter}"


class BoxMix(Dish):
    box_food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    box_drink = models.ForeignKey(
        Drink, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    box_sauce = models.ForeignKey(
        Sauce, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    box_dessert = models.ForeignKey(
        Dessert, on_delete=models.DO_NOTHING, blank=True, null=True
    )

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        price_list = [self.box_food, self.box_dessert, self.box_sauce, self.box_drink]
        self.price = (
            sum([element.price for element in price_list if element is not None])
            / 100
            * 85
        )
        super().save()


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"


class OrderItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    count = models.IntegerField()

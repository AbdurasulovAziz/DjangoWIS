from django.contrib import admin
from app import models
# Register your models here.


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Drink)
class DrinkAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Sauce)
class SauceAdmin(admin.ModelAdmin):
    pass

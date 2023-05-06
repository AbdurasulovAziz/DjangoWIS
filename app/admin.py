from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(FoodMenu)
admin.site.register(Sause)
admin.site.register(DrinkMenu)


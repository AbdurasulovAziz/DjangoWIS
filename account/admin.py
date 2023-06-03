from django.contrib import admin
from django.contrib.auth.models import Permission

from account import models
from account.models import CustomUser, Profile

admin.site.register(Permission)
# Register your models here.


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
    )
    search_fields = ("name",)


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "phone",
        "birth_day",
        "region",
    )

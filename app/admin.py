from django.contrib import admin

from .models import User, Profile
# Register your models here.



class ProfileAdmin(admin.TabularInline):
    model = Profile
    extra = 0


class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileAdmin]



admin.site.register(User, UserAdmin)

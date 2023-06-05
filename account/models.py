from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
import datetime

from account.managers import CustomUserManager
from account.validators import birth_date_validation


# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    first_name = models.CharField("First name", blank=True)
    last_name = models.CharField("Last name", blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(
        "Phone", validators=[RegexValidator("[+]\d+$")], blank=True
    )
    birth_day = models.DateField(
        "Birth day", validators=[birth_date_validation], blank=True, null=True
    )
    region = models.CharField("Region", blank=True)

    @property
    def age(self):
        result = datetime.date.today() - self.birth_day
        return result.days // 365

    def __str__(self):
        return self.user.email

# Generated by Django 4.2 on 2023-05-19 08:26

import account.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_if_profile_verified_customuser_if_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_day',
            field=models.DateField(blank=True, default=django.utils.timezone.now, validators=[account.validators.birth_date_validation], verbose_name='Birth day'),
            preserve_default=False,
        ),
    ]
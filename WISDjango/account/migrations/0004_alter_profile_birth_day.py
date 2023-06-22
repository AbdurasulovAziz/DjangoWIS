# Generated by Django 4.2 on 2023-05-19 08:27

import account.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_birth_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_day',
            field=models.DateField(blank=True, default='', validators=[account.validators.birth_date_validation], verbose_name='Birth day'),
        ),
    ]

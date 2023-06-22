# Generated by Django 4.2 on 2023-05-23 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_boxmix_dessert_alter_boxmix_drink_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxmix',
            name='on_stop',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dessert',
            name='on_stop',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='drink',
            name='on_stop',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='food',
            name='on_stop',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sauce',
            name='on_stop',
            field=models.BooleanField(default=False),
        ),
    ]

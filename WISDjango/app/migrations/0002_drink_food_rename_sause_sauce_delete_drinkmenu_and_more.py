# Generated by Django 4.2 on 2023-05-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('price', models.IntegerField()),
                ('category', models.CharField(choices=[('Cold', 'Cold Drinks'), ('Hot', 'Hot Drinks')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('price', models.IntegerField()),
                ('category', models.CharField(choices=[('Burger', 'Burger'), ('Twister', 'Twister'), ('Buckets', 'Buckets')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='Sause',
            new_name='Sauce',
        ),
        migrations.DeleteModel(
            name='DrinkMenu',
        ),
        migrations.DeleteModel(
            name='FoodMenu',
        ),
    ]

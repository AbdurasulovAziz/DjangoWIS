# Generated by Django 4.2 on 2023-05-25 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_order_product_order_user_orderitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DishModel',
            new_name='Dish',
        ),
        migrations.RenameField(
            model_name='dessert',
            old_name='dishmodel_ptr',
            new_name='dish_ptr',
        ),
        migrations.RenameField(
            model_name='drink',
            old_name='dishmodel_ptr',
            new_name='dish_ptr',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='dishmodel_ptr',
            new_name='dish_ptr',
        ),
        migrations.RenameField(
            model_name='sauce',
            old_name='dishmodel_ptr',
            new_name='dish_ptr',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='boxmix',
            name='on_stop',
            field=models.BooleanField(),
        ),
    ]

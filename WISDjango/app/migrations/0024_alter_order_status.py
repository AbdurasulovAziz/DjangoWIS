# Generated by Django 4.2 on 2023-05-31 06:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0023_order_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[("Cart", "In Cart"), ("Sent", "Sent")], default="Cart"
            ),
        ),
    ]
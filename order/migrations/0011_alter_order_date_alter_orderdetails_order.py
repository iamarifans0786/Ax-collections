# Generated by Django 4.1.3 on 2023-06-12 06:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0010_alter_order_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 12, 11, 47, 3, 410861)
            ),
        ),
        migrations.AlterField(
            model_name="orderdetails",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_detail",
                to="order.order",
            ),
        ),
    ]

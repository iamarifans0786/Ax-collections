# Generated by Django 4.2.1 on 2023-06-12 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0012_alter_order_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 12, 18, 4, 27, 241025)
            ),
        ),
    ]

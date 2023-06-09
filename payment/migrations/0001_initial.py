# Generated by Django 4.2.1 on 2023-05-30 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("transaction_id", models.CharField(max_length=20)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Successfull", "Successfull"),
                            ("Pending", "Pending"),
                            ("Processing", "Processing"),
                            ("Failed", "Failed"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="order.order",
                    ),
                ),
            ],
        ),
    ]

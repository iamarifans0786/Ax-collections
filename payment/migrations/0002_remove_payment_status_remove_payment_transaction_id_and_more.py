# Generated by Django 4.2.1 on 2023-06-09 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="status",
        ),
        migrations.RemoveField(
            model_name="payment",
            name="transaction_id",
        ),
        migrations.AddField(
            model_name="payment",
            name="amount",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="payment",
            name="created_at",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="payment",
            name="payment_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="payment",
            name="payment_method",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="payment",
            name="payment_status",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
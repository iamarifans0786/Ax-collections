# Generated by Django 4.2.1 on 2023-05-30 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("brand", "0001_initial"),
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="brand",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="brand.brand"
            ),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.3 on 2023-06-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0005_ourteam_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="popular_blog_status",
            field=models.BooleanField(default=False),
        ),
    ]

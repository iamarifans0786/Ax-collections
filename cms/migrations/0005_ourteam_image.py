# Generated by Django 4.2.1 on 2023-06-03 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0004_ourteam_alter_blog_sub_title_alter_blog_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="ourteam",
            name="image",
            field=models.ImageField(default=1, upload_to="our_team"),
            preserve_default=False,
        ),
    ]

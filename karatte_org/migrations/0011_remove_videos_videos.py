# Generated by Django 4.0.4 on 2022-06-11 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karatte_org', '0010_carousel_remove_videos_videos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='videos',
        ),
    ]
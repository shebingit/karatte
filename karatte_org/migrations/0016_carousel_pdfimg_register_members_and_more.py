# Generated by Django 4.0.4 on 2022-07-15 13:39

from django.db import migrations, models
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('karatte_org', '0015_alter_moreconts_con_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='mdesig',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='members',
            name='mname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='members',
            name='mposition',
            field=models.CharField(max_length=40),
        ),
    ]

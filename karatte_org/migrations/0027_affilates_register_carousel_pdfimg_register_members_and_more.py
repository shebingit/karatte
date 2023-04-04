# Generated by Django 4.1 on 2023-04-04 05:41

from django.db import migrations, models
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('karatte_org', '0026_auto_20220829_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='affilates_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affreg_name', models.CharField(default='', max_length=200, null=True)),
                ('affvalid_from', models.DateField(default='', null=True)),
                ('affvalid_to', models.DateField(default='', null=True)),
                ('affclub', models.CharField(default='', max_length=250, null=True)),
                ('affrank', models.CharField(default='', max_length=250, null=True)),
                ('affstate', models.CharField(default='', max_length=250, null=True)),
                ('affdistrict', models.CharField(default='', max_length=250, null=True)),
                ('aff_status', models.CharField(default=0, max_length=10)),
                ('affreg_img', models.ImageField(default='', upload_to='image/regcheck')),
            ],
        ),
    ]

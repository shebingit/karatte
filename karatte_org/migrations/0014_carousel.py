# Generated by Django 4.0.4 on 2022-06-24 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karatte_org', '0013_members_asso_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carimage', models.ImageField(null=True, upload_to='carouselimages/')),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=150)),
            ],
        ),
    ]
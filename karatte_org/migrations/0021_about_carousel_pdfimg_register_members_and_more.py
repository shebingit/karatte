# Generated by Django 4.1 on 2022-08-14 16:06

from django.db import migrations, models
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('karatte_org', '0020_carousel_histoyrpdf_pdfimg_register_members_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ab_contents', models.TextField()),
            ],
        ),
        
    ]
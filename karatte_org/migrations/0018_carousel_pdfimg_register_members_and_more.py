# Generated by Django 4.0.4 on 2022-07-18 09:10

from django.db import migrations, models
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('karatte_org', '0017_carousel_check_register_members_pdfimg_and_more'),
    ]

    operations = [
      
        migrations.AlterField(
            model_name='check_register_members',
            name='check_reg_img',
            field=models.ImageField(upload_to='image/regcheck'),
        ),
    ]

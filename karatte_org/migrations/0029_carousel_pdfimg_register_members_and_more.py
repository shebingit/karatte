# Generated by Django 4.1 on 2022-08-26 16:05

from django.db import migrations, models
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('karatte_org', '0028_carousel_pdfimg_register_members_and_more'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='regforms',
            name='ev_subhead',
            field=models.CharField(default=32, max_length=20),
            preserve_default=False,
        ),
        
    ]

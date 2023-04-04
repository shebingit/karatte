# Generated by Django 4.1 on 2023-04-04 06:24

from django.db import migrations, models
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('karatte_org', '0027_affilates_register_carousel_pdfimg_register_members_and_more'),
    ]

    operations = [
     
        migrations.AlterField(
            model_name='affilates_register',
            name='aff_status',
            field=models.CharField(blank=True, default=0, max_length=10)
        ),
        migrations.AlterField(
            model_name='affilates_register',
            name='affclub',
            field=models.CharField(blank=True, max_length=250, null=True)
        ),
        migrations.AlterField(
            model_name='affilates_register',
            name='affdistrict',
            field=models.CharField(blank=True,  max_length=250, null=True)
        ),
        migrations.AlterField(
            model_name='affilates_register',
            name='affrank',
            field=models.CharField(blank=True,  max_length=250, null=True)
        ),
        migrations.AlterField(
            model_name='affilates_register',
            name='affreg_name',
            field=models.CharField(blank=True,  max_length=200, null=True)
        ),
        migrations.AlterField(
            model_name='affilates_register',
            name='affstate',
            field=models.CharField(blank=True, max_length=250, null=True)
        ),
        migrations.AlterField(
            model_name='affilates_register',
            name='affvalid_from',
            field=models.DateField(blank=True,  null=True)
        ),
        migrations.AlterField(
            model_name='affilates_register',
            name='affvalid_to',
            field=models.DateField(blank=True,  null=True)
        ),
    ]

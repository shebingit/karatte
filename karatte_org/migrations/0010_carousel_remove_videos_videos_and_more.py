# Generated by Django 4.0.4 on 2022-06-11 08:52

from django.db import migrations, models
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('karatte_org', '0009_remove_videos_videos_affiliation_affiliation_img_and_more'),
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
    
        migrations.AddField(
            model_name='affiliation',
            name='affiliation_img',
            field=models.ImageField(null=True, upload_to='file'),
        ),
        migrations.AddField(
            model_name='videos',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
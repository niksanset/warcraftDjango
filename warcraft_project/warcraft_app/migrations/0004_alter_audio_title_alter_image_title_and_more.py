# Generated by Django 4.2.7 on 2024-01-23 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warcraft_app', '0003_remove_image_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

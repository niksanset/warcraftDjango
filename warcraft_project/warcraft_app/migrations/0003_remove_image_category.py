# Generated by Django 4.2.7 on 2024-01-23 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warcraft_app', '0002_audio_category_image_video_delete_game_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
    ]

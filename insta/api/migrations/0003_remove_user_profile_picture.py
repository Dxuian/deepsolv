# Generated by Django 5.1.4 on 2024-12-28 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_followedby_remove_user_follows_user_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_picture',
        ),
    ]
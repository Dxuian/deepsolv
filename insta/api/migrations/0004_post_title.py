# Generated by Django 5.1.4 on 2024-12-28 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='hello', max_length=255),
            preserve_default=False,
        ),
    ]

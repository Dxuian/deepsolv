# Generated by Django 5.1.4 on 2024-12-28 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='Post title', max_length=255),
        ),
    ]

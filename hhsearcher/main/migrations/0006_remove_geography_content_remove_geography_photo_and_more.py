# Generated by Django 4.1.4 on 2023-01-10 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_geography_content_geography_photo_geography_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geography',
            name='content',
        ),
        migrations.RemoveField(
            model_name='geography',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='geography',
            name='title',
        ),
    ]

# Generated by Django 4.2.13 on 2024-06-19 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='slug', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]

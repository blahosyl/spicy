# Generated by Django 4.2.13 on 2024-05-31 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_alter_ingredient_preparation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['ingr_name']},
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingr_name',
            field=models.CharField(max_length=50),
        ),
    ]
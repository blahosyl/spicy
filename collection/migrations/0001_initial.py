# Generated by Django 4.2.13 on 2024-06-03 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingr_name', models.CharField(max_length=50)),
                ('preparation', models.CharField(blank=True, max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['ingr_name', 'preparation'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('excerpt', models.TextField(blank=True, max_length=1000)),
                ('instructions', models.TextField()),
                ('prep_time', models.PositiveIntegerField()),
                ('cook_time', models.PositiveIntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_on'],
            },
        ),
        migrations.CreateModel(
            name='IngredientQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('unit', models.CharField(blank=True, choices=[('g', 'grams'), ('kg', 'kilograms'), ('ml', 'milliliters'), ('l', 'liters'), ('pc', 'pieces'), ('tsp', 'teaspoons'), ('Tbsp', 'tablespoons'), ('cups', 'cups'), ('cloves', 'cloves')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='quantity', to='collection.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='collection.recipe')),
            ],
            options={
                'verbose_name': 'Ingredient quantity',
                'verbose_name_plural': 'Ingredient quantities',
            },
        ),
    ]

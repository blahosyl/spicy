from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(max_length=1000, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes"
    )
    instructions = models.TextField()
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    class Meta:
        """
        order from most to least recently updated
        """
        ordering = ["-updated_on"]
    
    def __str__(self):
        return f"{self.title} | {self.author}"

    
class Ingredient(models.Model):
    ingr_name = models.CharField(max_length=50, unique=True)
    preparation = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        order from most to least recently updated
        """
        ordering = ["ingr_name"]

    def __str__(self):
        string = f"{self.ingr_name}"
        if self.preparation:
            string += f", {self.preparation}"
        return string



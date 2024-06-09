from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(max_length=1000, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    instructions = models.TextField()
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
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

    def total_time(self):
        return self.prep_time + self.cook_time
    
class Ingredient(models.Model):
    ingr_name = models.CharField(max_length=50)
    preparation = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # order from most to least recently updated
        ordering = ["ingr_name", "preparation"]
        # exclude duplicates of the same ingr_name and preparation
        unique_together = [("ingr_name", "preparation")]


    def __str__(self):
        string = f"{self.ingr_name}"
        if self.preparation:
            string += f", {self.preparation}"
        return string


class IngredientQuantity(models.Model):
    quantity = models.DecimalField(
        max_digits=7, 
        decimal_places=2, 
        blank= True,
        null= True,
    )
    GR ='g'
    KG = 'kg'
    ML = 'ml'
    LI = 'l'
    PC = 'pc'
    TEASP = 'tsp'
    TBSP = 'Tbsp'
    CUP = 'cups'
    CL = 'cloves'
    UNIT_CHOICES = [
        (GR, 'grams'),
        (KG, 'kilograms'),
        (ML, 'milliliters'),
        (LI, 'liters'),
        (PC, 'pieces'),
        (TEASP, 'teaspoons'),
        (TBSP, 'tablespoons'),
        (CUP, 'cups'),
        (CL, 'cloves'),
    ]
    unit = models.CharField(
        choices=UNIT_CHOICES,
        blank=True,
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, 
        related_name="ingredients",
    )
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.PROTECT, 
        related_name="quantity",
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        How the name of the model is shown in the admin panel
        """
        verbose_name = "Ingredient quantity"
        verbose_name_plural = "Ingredient quantities"

    def __str__(self):
        if self.quantity:
            quantity_string = f"{self.quantity} {self.unit} of "
        else:
            quantity_string = "To taste: "
        string = quantity_string + f"{self.ingredient} | {self.recipe}"
        return string



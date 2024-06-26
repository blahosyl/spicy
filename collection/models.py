from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Recipe(models.Model):
    """
    The Recipe model EXCLUDING ingredients and attributes
    """
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
        """
        How instances of this model are shown in the admin panel
        """
        return f"{self.title} | {self.author}"

    def total_time(self):
        """
        Calculate total time from prep time and cook time
        """
        return self.prep_time + self.cook_time


class Ingredient(models.Model):
    """
    Ingredients globally available to all recipes
    """
    ingr_name = models.CharField(max_length=50)
    preparation = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # order alphabetically by ingr_name, then preparation
        ordering = ["ingr_name", "preparation"]
        # exclude duplicates of the same ingr_name and preparation
        unique_together = [("ingr_name", "preparation")]

    def __str__(self):
        """
        How instances of this model are shown in the admin panel
        """
        string = f"{self.ingr_name}"
        if self.preparation:
            string += f", {self.preparation}"
        return string


class IngredientQuantity(models.Model):
    """
    The intermediary model between Recipes and Ingredients,
    containing extra information for each instance
    """
    quantity = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
    )
    GR = 'g'
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
        """
        How instances of this model are shown in the admin panel
        """
        if self.quantity:
            quantity_string = f"{self.quantity} {self.unit} of "
        else:
            quantity_string = "To taste: "
        string = quantity_string + f"{self.ingredient} | {self.recipe}"
        return string


class Comment(models.Model):
    """
    Comments on recipes
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(
        default=False
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # no prefix: ascending order, - descending, ? random
        ordering = ["created_on"]
    # show recipes by title in admin panel

    def __str__(self):
        """
        How instances of this model are shown in the admin panel
        """
        return f"Comment {self.body} by {self.author} Appr: {self.approved}"


class Attribute(models.Model):
    """
    Globally available attributes
    """
    category = models.CharField(max_length=50)
    attr_value = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # order alphabetically by category, then attr_value
        ordering = ["category", "attr_value"]
        # exclude duplicates of the same category and attr_value
        unique_together = [("category", "attr_value")]

    def __str__(self):
        """
        How instances of this model are shown in the admin panel
        """
        return f"{self.category}: {self.attr_value}"


class RecipeAttribute(models.Model):
    """
    The intermediary model between Recipes and Attributes
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name="attributes",
    )
    attribute = models.ForeignKey(
        Attribute,
        on_delete=models.PROTECT,
        related_name="recipes",
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        How the name of the model is shown in the admin panel
        """
        verbose_name = "Recipe attribute"
        unique_together = [("recipe", "attribute")]
        # order alphabetically by attribute, then recipe
        ordering = ["attribute", "recipe"]

    def __str__(self):
        """
        How instances of this model are shown in the admin panel
        """
        string = f"{self.attribute} | {self.recipe}"
        return string

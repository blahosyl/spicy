from django.contrib import admin
from .models import Recipe, Ingredient, IngredientQuantity, RecipeAttribute, Attribute, Comment
from django_summernote.admin import SummernoteModelAdmin

class IngredientQuantityInline(admin.TabularInline):
    """
    Make this model available in another model's interface
    """
    model = IngredientQuantity


class RecipeAttributeInline(admin.TabularInline):
    """
    Make this model available in another model's interface
    """
    model = RecipeAttribute


class CommentInline(admin.TabularInline):
    """
    Make this model available in another model's interface
    """
    model = Comment

# Register your models here.

@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('instructions',)
    inlines = [IngredientQuantityInline, RecipeAttributeInline, CommentInline]

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    inlines = [IngredientQuantityInline]

@admin.register(Attribute)
class IngredientAdmin(admin.ModelAdmin):
  inlines = [RecipeAttributeInline]

# also register these models as stand-alone in the admin panel
admin.site.register(IngredientQuantity)
admin.site.register(RecipeAttribute)
admin.site.register(Comment)





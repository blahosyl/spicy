from django.contrib import admin
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Ingredient, IngredientQuantity, RecipeAttribute
from .models import Attribute, Comment


class IngredientQuantityInline(admin.TabularInline):
    """
    Make this model available in another model's interface
    """
    model = IngredientQuantity

    # for Staff users, only their recipes are available in the recipe field,
    # so they can only create new objects linked to their own recipes
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "recipe" and not request.user.is_superuser:
            kwargs["queryset"] = Recipe.objects.filter(author=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


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


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):
    """
    Enables the administration of Recipe objects, including related
    IngredientQuantity, RecipeAttribute and Commnent objects
    """

    list_display = ('title', 'slug')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('instructions',)
    inlines = [IngredientQuantityInline, RecipeAttributeInline, CommentInline]

    # staff users should only view, change & delete their own recipes
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    # for Staff users, only their username is available in the author field,
    # so they can only create new recipes linked to their own username
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author" and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(username=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Ingredient)

class IngredientAdmin(admin.ModelAdmin):
    """
    Enables the administration of Ingredient objects 
    and related IngredientQuantity objects
    """
    inlines = [IngredientQuantityInline]


@admin.register(Attribute)
class IngredientAdmin(admin.ModelAdmin):
    """
    Enables the administration of Attribute objects 
    and related RecipeAttribute objects
    """
    inlines = [RecipeAttributeInline]


class StaffAdmin(admin.ModelAdmin):
    """
    Restrict the Administration of certain objects for Staff users
    """

    # staff users can only view, change & delete their own objects
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(recipe__author=request.user)

    # for Staff users, only their recipes are available in the recipe field,
    # so they can only create new objects linked to their own recipes
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "recipe" and not request.user.is_superuser:
            kwargs["queryset"] = Recipe.objects.filter(author=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# also register "dependent" models as stand-alone in the admin panel
# staff users only create, view, change & delete ingredient quantities
# related to their own recipes
admin.site.register(IngredientQuantity, StaffAdmin)
# staff users only create view, change & delete recipe attributes
# related to their own recipes
admin.site.register(RecipeAttribute, StaffAdmin)
admin.site.register(Comment)

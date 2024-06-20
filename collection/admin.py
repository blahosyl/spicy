from django.contrib import admin
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, IngredientQuantity, RecipeAttribute, Attribute, Comment
from django_summernote.admin import SummernoteModelAdmin

class IngredientQuantityInline(admin.TabularInline):
    """
    Make this model available in another model's interface
    """
    model = IngredientQuantity

    # for Staff users, only their recipes are visible/available in the recipe field,
    # so they can only create new objects linked to their own recipes    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "recipe":
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

# Register your models here.

@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('instructions',)
    inlines = [IngredientQuantityInline, RecipeAttributeInline, CommentInline]

    # staff users (who are not superadmins) should only view, change & delete their own recipes
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    # for Staff users, only their username is visible/available in the author field,
    # so they can only create new recipes linked to their own username    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = User.objects.filter(username=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    inlines = [IngredientQuantityInline]

@admin.register(Attribute)
class IngredientAdmin(admin.ModelAdmin):
  inlines = [RecipeAttributeInline]

class StaffAdmin(admin.ModelAdmin):

    # staff users (who are not superadmins) can only view, change & delete their own objects
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(recipe__author=request.user)

    # for Staff users, only their recipes are visible/available in the recipe field,
    # so they can only create new objects linked to their own recipes
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "recipe":
            kwargs["queryset"] = Recipe.objects.filter(author=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# also register these models as stand-alone in the admin panel
#staff users only create, view, change & delete ingredient quantities
# related to their own recipes
admin.site.register(IngredientQuantity, StaffAdmin)
#staff users only create view, change & delete recipe attributes
# related to their own recipes
admin.site.register(RecipeAttribute, StaffAdmin)
admin.site.register(Comment)





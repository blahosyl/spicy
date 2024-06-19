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

    # staff users (who are not superadmins) should only view, change & delete their own recipes
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    inlines = [IngredientQuantityInline]

@admin.register(Attribute)
class IngredientAdmin(admin.ModelAdmin):
  inlines = [RecipeAttributeInline]

# staff users (who are not superadmins) should only view, change & delete their own objects
class StaffAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(recipe__author=request.user)


# also register these models as stand-alone in the admin panel
#staff users only view, change & delete their own ingredient quantities
admin.site.register(IngredientQuantity, StaffAdmin)
#staff users only view, change & delete their own recipe attributes
admin.site.register(RecipeAttribute, StaffAdmin)
admin.site.register(Comment)





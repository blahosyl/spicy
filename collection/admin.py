from django.contrib import admin
from .models import Recipe, Ingredient, IngredientQuantity
from django_summernote.admin import SummernoteModelAdmin

# Register your models here

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', )
    search_fields = ['title']
    list_filter = ('author',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('instructions', )


admin.site.register(Ingredient)
admin.site.register(IngredientQuantity)




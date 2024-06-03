from django.contrib import admin
from .models import Recipe, Ingredient, IngredientQuantity
from django_summernote.admin import SummernoteModelAdmin

class IngredientQuantityInline(admin.TabularInline):
    model = IngredientQuantity

@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('instructions',)
    inlines = [IngredientQuantityInline]


# Register your models here.
admin.site.register(IngredientQuantity)

admin.site.register(Ingredient)




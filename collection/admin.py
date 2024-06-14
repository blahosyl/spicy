from django.contrib import admin
from .models import Recipe, Ingredient, IngredientQuantity, Comment
from django_summernote.admin import SummernoteModelAdmin

class IngredientQuantityInline(admin.TabularInline):
    model = IngredientQuantity


class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('instructions',)
    inlines = [IngredientQuantityInline, CommentInline]

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    inlines = [IngredientQuantityInline]


# Register your models here.
admin.site.register(IngredientQuantity)




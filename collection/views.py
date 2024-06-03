from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(published=True)
    template_name = "collection/index.html"
    paginate_by = 6

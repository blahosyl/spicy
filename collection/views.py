from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.
class RecipeList(generic.ListView):
    model = Recipe

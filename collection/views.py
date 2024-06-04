from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe

# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(published=True)
    template_name = "collection/index.html"
    paginate_by = 6


def recipe_detail(request, slug):
    """
    Display an individual :model:`collection.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`collection.Recipe`.

    **Template:**

    :template:`collection/recipe_detail.html`
    """

    queryset = Recipe.objects.filter(published=True)
    recipe = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "collection/recipe_detail.html",
        {"recipe": recipe},
    )

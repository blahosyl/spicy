from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Recipe
from .forms import CommentForm


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
    # `ingredients` is the `related_name` for the Recipe model in the IngredientQuantity model
    recipe_ingredients = recipe.ingredients.all()
    ingredient_count = recipe_ingredients.count()
    comments = recipe.comments.all()
    comment_count = recipe.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    comment_form = CommentForm()

    return render(
        request,
        "collection/recipe_detail.html",
        {"recipe": recipe,
        "recipe_ingredients": recipe_ingredients,
        "ingredient_count": ingredient_count,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )

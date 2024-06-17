from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Recipe, Comment
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
    recipe_attributes = recipe.attributes.all()
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
        "recipe_attributes": recipe_attributes,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Recipe.objects.filter(published=True)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
     """
    queryset = Recipe.objects.filter(published=True)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


# based on https://learndjango.com/tutorials/django-search-tutorial
class SearchResultsView(generic.ListView):
        model = Recipe
        template_name = 'collection/search_results.html'
        paginate_by = 6


        def get_queryset(self): 
            query = self.request.GET.get("q")
            object_list = Recipe.objects.filter(
                Q(title__icontains=query) 
                | Q(excerpt__icontains=query)
                | Q(instructions__icontains=query)
                | Q(comments__body__icontains=query) # with the help of Roman Rakic
                # | Q(attributes__attribute__attr_value__icontains=query)
                # | Q(ingredients__ingredient__ingr_name__icontains=query)

            )
            return object_list

        # add query to context, so it can be displayed on the search page
        def get_context_data(self, **kwargs):
            context = super(SearchResultsView, self).get_context_data(**kwargs)
            context['query'] = self.request.GET.get('q')
            return context
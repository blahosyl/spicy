from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Recipe, Comment
from .forms import CommentForm


class RecipeList(generic.ListView):
    """
    Provide a paginated list of all published recipes
    """
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
    # `ingredients` is the `related_name` for the Recipe model
    # in the IngredientQuantity model
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
                'Comment submitted and awaiting approval',
                extra_tags='comment'
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
    View to edit comments
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
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Comment updated!',
                                 extra_tags='comment')
        else:
            messages.add_message(request,
                                 messages.ERROR,
                                 'Error updating comment!',
                                 extra_tags='comment')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete comment
    """
    queryset = Recipe.objects.filter(published=True)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request,
                             messages.SUCCESS,
                             'Comment deleted!',
                             extra_tags='comment')
    else:
        messages.add_message(request,
                             messages.ERROR,
                             'You can only delete your own comments!',
                             extra_tags='comment')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


# based on https://learndjango.com/tutorials/django-search-tutorial
class SearchResultsView(generic.ListView):
    """
    Provide a list of recipes matching the search query
    """
    model = Recipe
    template_name = 'collection/search_results.html'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Recipe.objects.filter(
            Q(title__icontains=query)
            | Q(excerpt__icontains=query)
            | Q(instructions__icontains=query)
            | Q(comments__body__icontains=query)
            # querying of related models implemented with help from Roman Rakic
            | Q(attributes__attribute__attr_value__icontains=query)
            | Q(ingredients__ingredient__ingr_name__icontains=query)
        ).distinct()
        return object_list

    # add query to context, so it can be displayed on the results page
    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        context['object_count'] = self.object_list.count()
        return context


class FilterResultsView(generic.ListView):
    """
    Provide filtered recipes using the following dropdown forms:
    temp
    diet
    taste
    texture
    """
    model = Recipe
    template_name = 'collection/index.html'
    paginate_by = 6

    def get_queryset(self):
        temp = self.request.GET.get("temp")
        diet = self.request.GET.get("diet")
        taste = self.request.GET.get("taste")
        texture = self.request.GET.get("texture")
        object_list = Recipe.objects.all()
        if temp:
            query = temp
        if diet:
            query = diet
        if taste:
            query = taste
        if texture:
            query = texture
        if query == "any temperature" or query == "any diet" \
                or query == "any taste" or query == "any texture":
            object_list = Recipe.objects.all()
        else:
            object_list = Recipe.objects.filter(
                Q(attributes__attribute__attr_value__icontains=query)
            ).distinct()
        return object_list

    # add filters and object count to context,
    # so they can be displayed on the results page
    def get_context_data(self, **kwargs):
        context = super(FilterResultsView, self).get_context_data(**kwargs)
        context['object_count'] = self.object_list.count()
        context['temp'] = self.request.GET.get('temp')
        context['diet'] = self.request.GET.get('diet')
        context['taste'] = self.request.GET.get('taste')
        context['texture'] = self.request.GET.get('texture')
        return context

from . import views
from .views import SearchResultsView, FilterResultsView
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("filter/", FilterResultsView.as_view(), name="filter_results"),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]

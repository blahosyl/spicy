from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_profiles, name='community'),
    path('<slug:slug>/', views.profile_detail, name='profile_detail'),
]
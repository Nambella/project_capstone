from django.urls import path
from .views import RecipeListCreateView, RecipeDetailView, UserCreateView

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('users/', UserCreateView.as_view(), name='user-create'),
]

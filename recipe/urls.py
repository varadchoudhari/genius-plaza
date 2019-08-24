from .views import RecipeView, UserRecipeView
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('recipes', RecipeView)

urlpatterns = [
    path('', include(router.urls)),
    path('recipes/user/<int:user>/', UserRecipeView.as_view({'get': 'get'}))
]
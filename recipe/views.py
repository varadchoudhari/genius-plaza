from .models import Recipe
from .serializers import RecipeSerializer
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class RecipeView(viewsets.ModelViewSet):
    """
    View representing the recipe API.
    Handles GET, POST, PATCH, DELETE
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class UserRecipeView(viewsets.ViewSet):
    """
    View representing the User and Recipe relation.
    Handles GET request
    """
    def get(self, request, user=None):
        """
        Gets all the recipes by particular user. If User
        does not exists, returns 404
        """
        if not User.objects.filter(id=user).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        recipes_by_user = Recipe.objects.filter(user=user)
        serializer = RecipeSerializer(recipes_by_user, many=True)
        return Response(serializer.data)

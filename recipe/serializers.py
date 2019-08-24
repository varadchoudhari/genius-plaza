from .models import Recipe, Step, Ingredient
from rest_framework import serializers

class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Recipe
    """
    class Meta:
        """
        Defining the metadata
        """
        model = Recipe
        # Returns the following fields in the response
        fields = ('id', 'name', 'user')



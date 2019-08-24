from django.contrib.auth.models import User
from django.db import models

class Recipe(models.Model):
    """
    The model representing the recipe
    """

    # Using CharField as this is the name of the recipe and for now
    # we can safely assume that it won't go beyond 100 characters
    name = models.CharField(max_length=100, null=False)

    # We don't want recipe without user, so if User is deleted
    # we will delete the Recipe as well
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Step(models.Model):
    """
    The model representing the steps of the recipe
    """

    # Using TextField as some recipies may have more steps than others
    # so using TextField will make the app scalable without the need
    # to run migrations again in future
    step_text = models.TextField(null=False)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.step_text


class Ingredient(models.Model):
    """
    The model representing the ingredients of the recipe
    """

    # Using TextField as some recipes may have more ingredients than others
    # so using TextField will make the app scalable without the need
    # to run migrations again in future
    text = models.TextField(null=False)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

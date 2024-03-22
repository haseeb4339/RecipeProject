from django.shortcuts import render


def Recipes(request):

    return render(request, 'recipes.html')
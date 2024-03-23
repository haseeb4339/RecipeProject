from django.shortcuts import render, redirect
from .models import Recipe


def Recipes(request):

    if request.method == "POST":
        data = request.POST
        
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image



        )

        return redirect('/recipes/')
    
    queryset = Recipe.objects.all()

    context = {'Recipes': queryset}

    return render(request, 'recipes.html', context)
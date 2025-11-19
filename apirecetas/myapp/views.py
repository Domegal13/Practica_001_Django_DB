import json
from django.shortcuts import render
from django.http import HttpResponse
from .  import models   

# Create your views here.
def index(request):
    try:
        all_recipes = models.Recipes.objects.all()
        recipes_json = []
        for recipe in all_recipes:
            new_recipe = {
                'id' : recipe.id,
                'name' : recipe.name,
                'ingredients' : recipe.ingredients,
                'preparation':recipe.preparation,
                'onMenu' : recipe.onMenu,
                'people' : recipe.people
            }
            recipes_json.append(new_recipe)
        recipes_json = json.dumps(recipes_json, ensure_ascii=False).encode('utf8')
    except Exception as error:
        print(f'Error: {error}') 
           
    return HttpResponse(recipes_json)





# new_recipe = models.Recipes(
#         name = 'Picante de Carne',
#         ingredients = '''
#                         400 Gramos de Carne de Res
#                         1 Unidad de MAGGI® Cubo Carne
#                         4 Papas Blancas
#                         2 Zanahorias
#                         1/2 Taza de Alverjas
#                         1 Cebolla Roja
#                         1 Cucharadita de Ajo Molido
#                         1 Cucharada de Ají Panca Molido
#                         2 Cucharadas de Aceite Vegetal
#                         2 Tazas de Arroz Cocido
#                     ''',
#         preparation = ''' 
#                         1.Pelar y cortar la cebolla y la zanahoria en cubos pequeños y las papas en cubos grandes. Cortar la carne de res en cubos grandes.
#                         2.En una sartén, calentar el aceite y agregar la cebolla, dejar sudar por 5 minutos. Incorporar el ajo, el ají panca y un cubo MAGGI® Sabor Carne.
#                         3.Incorporar los cubos de carne, papa y 2 tazas de agua. Cocinar por 30 minutos. Finalmente, agregar la zanahoria, las alverjas y terminar de cocinar por 5 minutos más. Retirar la olla del calor.
#                         4.Servir el picante de carne, acompañado de media taza de arroz.
#                     ''',
#         onMenu = False,
#         people = 4,
#     )
#     new_recipe.save()
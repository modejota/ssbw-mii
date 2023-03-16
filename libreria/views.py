from django.shortcuts import render
from libreria.models import Libro

# Imagino que en algún momento se sustituirá por un index hecho y derecho.
def home(request):
    return render(request, 'base.html', context=None)

def busqueda(request, query):
    libros = Libro.objects.filter(title__icontains=query)
    context = {
        'busqueda': query,
        'libros': libros
        }
    return render(request, 'busqueda.html', context=context)

def buscar(request):
    query = request.POST.get('query')
    if query is None:
        query = ""
    # Debería hacerse una validación de la query, y si es vacía mostrar otro menú de buscador.
    #  Pero por ahora no lo ha dicho, asi que hago el apaño para que en query vacia muestre todo.
    return busqueda(request, query)
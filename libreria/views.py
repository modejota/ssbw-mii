from django.shortcuts import render, redirect
from libreria.models import Libro
from libreria.forms import FormularioLibro
import logging
logger = logging.getLogger(__name__)

# Por ahora he puesto de página de inicio el listado de libros.
def home(request):
    return buscar(request)

def buscar(request):
    query = request.POST.get('query')
    if query is None:
        query = ""
    libros = Libro.objects.filter(title__icontains=query)
    logger.info("Buscando: %s", query)
    # Debería hacerse una validación de la query, y si es vacía mostrar otro menú de buscador.
    # Pero por ahora no lo ha dicho, asi que hago el apaño para que en query vacia muestre todo.
    context = {
        'busqueda': query,
        'libros': libros
        }
    return render(request, 'busqueda.html', context=context)

def añadir(request):
    formulario = FormularioLibro()
    if request.method == 'POST':
        formulario = FormularioLibro(request.POST)
        if formulario.is_valid():
            logger.debug("Añadiendo libro: %s", formulario.cleaned_data)
            formulario.save()      # Esto hay que cambiarlo, el formulario no tiene método save
            return redirect('buscar')
    context = {
        'form': formulario
    }
    return render(request, 'añadir.html', context=context)

def detalle(request, id):
    # Buscar en la BD
    context = {
        'id': id,
    }
    return render(request, 'detalle.html', context=context)
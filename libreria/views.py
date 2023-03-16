from django.shortcuts import render
from django.http import HttpResponse
from libreria.models import Libro

def home(request):
    return render(request, 'base.html', context=None)

def busqueda(request, query):
    libros = Libro.objects.filter(title__icontains=query)
    # Aquí vendría la plantilla que muestra los resultados
    context = {
        'busqueda': query,
        'libros': libros
        }
    return render(request, 'busqueda.html', context=context)

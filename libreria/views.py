from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def buscar(request):
    # Se supone que aquí se haría la búsqueda
    return render(request, 'buscar.html', context=None)

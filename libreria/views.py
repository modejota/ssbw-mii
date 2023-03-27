from django.contrib import messages
from django.shortcuts import render, redirect
from libreria.models import Libro
from libreria.forms import FormularioLibro
from datetime import timedelta
import logging
logger = logging.getLogger(__name__)

def home(request):
    # Por ahora he puesto de página de inicio el listado de todos los libros.
    return buscar(request)

def buscar(request):
    query = request.POST.get('query')
    if query is None:   # Por si se quita el required en HTML maliciosamente.
        query = ""
    libros = Libro.objects.filter(title__icontains=query)
    if query != "":     # No mostrar el mensaje si no se ha buscado nada. (Cuando se viene de home)
        logger.info("Buscando: %s", query)
    context = {
        'busqueda': query,
        'libros': libros
        }
    return render(request, 'busqueda.html', context=context)

def aniadir(request):
    formulario = FormularioLibro()
    if request.method == 'POST':
        formulario = FormularioLibro(request.POST)
        if formulario.is_valid():
            libro = Libro(
                author=formulario.cleaned_data['author'],
                title=formulario.cleaned_data['title'],
                genre=formulario.cleaned_data['genre'],
                description=formulario.cleaned_data['description'],
                isbn=formulario.cleaned_data['isbn'],
                published=formulario.cleaned_data['published'],
                publisher=formulario.cleaned_data['publisher'],
            )
            try:    # Si el ISBN ya existe, no se añade. Notificamos del estado al usuario.
                Libro.objects.insert(libro, load_bulk=False)
                logger.info("Añadiendo: %s", libro.isbn)
                messages.success(request, 'El libro ha sido añadido correctamente.')
            except:
                logger.warning("No se ha podido añadir el libro con isbn: %s", libro.isbn)
                messages.error(request, 'Ha ocurrido un error al añadir el libro.')
            return redirect('aniadir')

    context = {
        'form': formulario
    }
    return render(request, 'aniadir.html', context=context)

def detalle(request, id):
    libro = Libro.objects(isbn=str(id)).first()
    if libro is None:
        logger.warning("No se ha encontrado el libro con isbn: %s", id)
        # La plantilla contempla el mensaje de error.
    context = {
        'isbn': id,
        'libro': libro,
    }
    return render(request, 'detalle.html', context=context)

def editar(request, id):
    formulario = FormularioLibro()
    if request.method == 'POST':
        formulario = FormularioLibro(request.POST)
        if formulario.is_valid():
            try:
                Libro.objects(isbn=str(id)).update_one(
                    author=formulario.cleaned_data['author'],
                    title=formulario.cleaned_data['title'],
                    genre=formulario.cleaned_data['genre'],
                    description=formulario.cleaned_data['description'],
                    isbn=formulario.cleaned_data['isbn'],
                    published=formulario.cleaned_data['published']+timedelta(days=1),
                    # Suma un día porque mongoengine lo guarda con un día menos al tener en cuenta la hora 00:00:00 según ISO 8601 y el navegador ignorarlo.
                    publisher=formulario.cleaned_data['publisher'],
                )
                logger.info("Editando: %s", id)
                messages.success(request, 'El libro ha sido editado correctamente.')
            except:
                logger.warning("No se ha podido editar el libro con isbn: %s", id)
                messages.error(request, 'Ha ocurrido un error al editar el libro. Posiblemente el ISBN ya exista.')
            return redirect('editar', id)

    try:    # Modificar HTML maliciosamente puede provocar un error.
        libro = Libro.objects(isbn=str(id)).first()
    except:
        logger.warning("No se ha podido editar el libro con isbn: %s", id)
        messages.error(request, 'Ha ocurrido un error al editar el libro.')
        return redirect('home')

    formulario = FormularioLibro(initial={
        'author': libro.author,
        'title': libro.title,
        'genre': libro.genre,
        'description': libro.description,
        'isbn': libro.isbn,
        'published': libro.published,
        'publisher': libro.publisher,
    })
    context = {
        'isbn': id,
        'form': formulario,
    }
    return render(request, 'editar.html', context=context)

def eliminar(request, id):
    # Django no admite DELETE en formularios, por lo que usamos POST. No usamos GET porque se podría eliminar un libro sin querer haciendo uso de URL.
    if request.method == 'POST':
        docs_deleted = Libro.objects(isbn=str(id)).delete()
        if docs_deleted == 0:
            logger.warning("No se ha podido eliminar el libro con isbn: %s", id)
            messages.error(request, 'Ha ocurrido un error al eliminar el libro.')
        else:
            logger.info("Eliminando: %s", id)
            messages.success(request, 'El libro ha sido eliminado correctamente.')
    else:
        logger.warning('Intento de eliminar libro %s con GET.', id)
        messages.warning(request, 'Para eliminar libros utilice el apartado de la web correspondiente.')
    return redirect('home')
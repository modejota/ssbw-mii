from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from libreria.models import Libro
from libreria.forms import FormularioLibro
from datetime import timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging
logger = logging.getLogger(__name__)

def home(request):
    # Optamos por mostrar directamente los libros en la página principal.
    return buscar(request)

def buscar(request):
    query = request.POST.get('query')
    if query is None:   # Por si se quita el required en HTML maliciosamente.
        query = ""
    libros = Libro.objects.filter(title__icontains=query).only("isbn", "title", "author")   # Sólo se muestran los campos necesarios, ahorrando ancho de banda.
    if query != "":     # No mostrar el mensaje si no se ha buscado nada. (Cuando se viene de home)
        logger.info("Buscando: %s", query)
    context = {
        'busqueda': query,
        'libros': libros
        }
    return render(request, 'busqueda.html', context=context)

def aniadir(request):
    if not request.user.is_staff:
        logger.error("Se ha intentado acceder a la página de añadir libro sin permisos.")
        messages.error(request, 'No tiene permisos para acceder a operaciones de modificación sobre la base de datos. Por favor, inicie sesión como miembro del staff.')
        return redirect('login')    # Podría redirigir a home en su lugar

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
    if not request.user.is_staff:
        logger.error("Se ha intentado acceder a la página de editar libro sin permisos.")
        messages.error(request, 'No tiene permisos para acceder a operaciones de modificación sobre la base de datos. Por favor, inicie sesión como miembro del staff.')
        return redirect('login')    # Podría redirigir a home en su lugar

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
    if not request.user.is_staff:
        logger.error("Se ha intentado acceder a la página de eliminar libro sin permisos.")
        messages.error(request, 'No tiene permisos para acceder a operaciones de modificación sobre la base de datos. Por favor, inicie sesión como miembro del staff.')
        return redirect('login')    # Podría redirigir a home en su lugar

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
        # Podría mostrarse como error, pero es más bien una advertencia.
        logger.warning('Intento de eliminar libro %s con GET.', id)
        messages.warning(request, 'Para eliminar libros utilice el apartado de la web correspondiente.')
    return redirect('home')

def signup(request):
    if request.user.is_authenticated:
        logger.warning('Intento de registro de usuario ya autenticado.')
        messages.warning(request, 'Ya ha iniciado sesión. No es necesario registrarse.')
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # El formulario ya comprueba que las contraseñas coinciden, pero aseguramos por si se manipula el HTML/JS.
            raw_password = form.cleaned_data.get('password1')
            confirm_password = form.cleaned_data.get('password2')
            if raw_password != confirm_password:
                logger.error('Las contraseñas no coinciden al intentar registrar usuario %s.', username)
                messages.error(request, 'Las contraseñas no coinciden.')
                return redirect('signup')

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            logger.info('Usuario %s registrado.', username)
            messages.success(request, 'Usuario registrado correctamente. Se ha iniciado sesión automáticamente.')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def my_login(request):
    if request.user.is_authenticated:
        logger.warning('Intento de inicio de sesión de usuario ya autenticado.')
        messages.warning(request, 'Ya ha iniciado sesión. No es necesario volver a hacerlo.')
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                logger.info('Usuario %s inició sesión.', username)
                messages.success(request, 'Inicio de sesión correcto.')
                return redirect('home')
            else:
                logger.warning('Usuario %s no pudo iniciar sesión.', username)
                messages.error(request, 'Usuario o contraseña incorrectos.')
                return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def busqueda_reactiva(request):
    search_query = request.GET.get('search', '')
    if search_query is None:
        search_query = ""
    libros = Libro.objects(title__icontains=search_query).only("isbn", "title", "author") # Sólo se muestran los campos necesarios, ahorrando ancho de banda.
    data = [{'title': libro.title, 'author': libro.author, 'isbn': libro.isbn} for libro in libros]
    if search_query != "":
        logger.info("Buscando: %s", search_query, "via API")
    return JsonResponse({'books': data})

########## API ##########
from libreria.serializer import LibroSerializer

def get_libro_or_404(isbn):
    try:
        return Libro.objects.get(isbn=isbn)
    except Libro.DoesNotExist:
        return Response({'error': 'Libro no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

class LibrosAPI(APIView):

    def get(self, request):
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)
        logger.info("Listando libros via API")
        return Response(serializer.data)

class LibroAPI(APIView):

    def get(self, request, isbn):
        libro = get_libro_or_404(isbn)
        serializer = LibroSerializer(libro)
        logger.info("Listando libro con ISBN %s via API", isbn)
        return Response(serializer.data)


    def post(self, request, isbn):
        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Creando libro con ISBN %s via API", isbn)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, isbn):
        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Actualizando libro con ISBN %s via API", isbn)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, isbn):
        libro = get_libro_or_404(isbn)
        libro.delete()
        logger.info("Eliminando libro con ISBN %s via API", isbn)
        return Response(status=status.HTTP_204_NO_CONTENT)

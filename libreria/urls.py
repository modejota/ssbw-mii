from django.urls import path
from libreria import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buscar/', views.buscar, name='buscar'),
    path('añadir/', views.aniadir, name='añadir'),
    path('detalle/<int:id>', views.detalle, name='detalle'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('accounts/login/', views.my_login, name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('busqueda_reactiva/libros/', views.busqueda_reactiva, name='libro-busqueda-reactiva'),
    path('api/libros/', views.LibrosAPI.as_view(), name='API-libros-y-crear'),
    path('api/libros/<str:isbn>', views.LibroAPI.as_view(), name='API-manejar-libro-individual'),
]

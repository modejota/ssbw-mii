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
]

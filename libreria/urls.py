from django.urls import path
from libreria import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buscar/', views.buscar, name='buscar'),
    path('añadir/', views.añadir, name='añadir'),
    path('detalle/<int:id>', views.detalle, name='detalle'),
]
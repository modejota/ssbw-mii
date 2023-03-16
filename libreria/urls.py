from django.urls import path
from libreria import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buscar/<str:query>', views.busqueda, name='busqueda')
]
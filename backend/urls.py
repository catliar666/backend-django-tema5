"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from projects.views import create_personaje, find_personaje, update_personaje, delete_personaje, todos, find_usuarios

urlpatterns = [
    path("todos/", todos, name="crear_personaje"),
    path("usuarios/", find_usuarios, name="find_usuarios"),
    path("crear/", create_personaje, name="crear_personaje"),
    path("buscar/<str:id>/", find_personaje, name="buscar_personaje"),
    path("buscar/", find_personaje, name="buscar_personaje"),
    path("editar/<str:id>/", update_personaje, name="editar_personaje"),
    path("eliminar/<str:id>/", delete_personaje, name="eliminar_personaje"),
]


"""animespedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import include
from animes.views import inicio
from animes.views import inicio_snk
from animes.views import galeria_snk
from animes.views import personajes_snk
from animes.views import formulario_snk
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('animes/', include('animes.urls')),
    path ("", inicio, name="inicio"),
    path ("inicio_snk/", inicio_snk, name="inicio_snk"),
    path ("galeria_snk/", galeria_snk, name="galeria_snk"),
    path ("personajes_snk/", personajes_snk, name="personajes_snk"),
    path ("formulario_snk/", formulario_snk, name="formulario_snk"),
]

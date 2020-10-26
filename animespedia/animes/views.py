from django.shortcuts import render

def inicio (request):
    return render(request, "animes/base_inicio.html")
def inicio_snk (request):
    return render(request, "animes/base_inicio_snk.html")
def galeria_snk (request):
    return render(request, "animes/base_galeria_snk.html")
def personajes_snk (request):
    return render(request, "animes/base_personajes_snk.html")
def formulario_snk (request):
    return render(request, "animes/base_formulario_snk.html")
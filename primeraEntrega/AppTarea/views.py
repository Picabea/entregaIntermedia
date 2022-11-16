from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.


def crear_curso(request):
    
    if request.method == 'POST':
        
        formulario = CrearCurso(request.POST)

        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data

        curso = Curso(nombre=formulario_limpio['nombre'], comision=formulario_limpio['comision'])
        curso.save()

        return render(request, 'index.html')
    else:
        formulario = CrearCurso()

    return render(request, 'crear_curso.html', {'formulario': formulario})

def buscar_curso(request):
    
    if request.GET.get('nombre', False):
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains=nombre)

        return render(request, "buscar_curso.html", {'cursos': cursos})
    else:
        respuesta = "No hay datos"
        
    return render(request, 'buscar_curso.html', {'respuesta': respuesta})

def crear_edificio(request):
    
    if request.method == 'POST':
        
        formulario1 = CrearEdificio(request.POST)

        if formulario1.is_valid():
            formulario_limpio = formulario1.cleaned_data

        edificio = Edificio(pisos=formulario_limpio['pisos'], facultad=formulario_limpio['facultad'], cantidad_de_aulas=formulario_limpio['cantidad_de_aulas'])
        edificio.save()

        return render(request, 'index.html')
    else:
        formulario1 = CrearEdificio()

    return render(request, 'crear_edificio.html', {'formulario1': formulario1})

def buscar_edificio(request):
    
    if request.GET.get('facultad', False):
        facultad = request.GET['facultad']
        edificios = Edificio.objects.filter(facultad__icontains=facultad)

        return render(request, "buscar_edificio.html", {'edificios': edificios})
    else:
        respuesta = "No hay datos"
        
    return render(request, 'buscar_edificio.html', {'respuesta': respuesta})

def crear_aula(request):
    
    if request.method == 'POST':
        
        formulario2 = CrearAula(request.POST)

        if formulario2.is_valid():
            formulario_limpio = formulario2.cleaned_data

        aula = Aula(materia=formulario_limpio['materia'], numero=formulario_limpio['numero'], tamaño=formulario_limpio['tamaño'])
        aula.save()

        return render(request, 'index.html')
    else:
        formulario2 = CrearAula()

    return render(request, 'crear_aula.html', {'formulario2': formulario2})

def buscar_aula(request):
    
    if request.GET.get('numero', False):
        numero = request.GET['numero']
        aulas = Aula.objects.filter(numero__icontains=numero)

        return render(request, "buscar_aula.html", {'aulas': aulas})
    else:
        respuesta = "No hay datos"
        
    return render(request, 'buscar_aula.html', {'respuesta': respuesta})

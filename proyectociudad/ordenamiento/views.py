from django.shortcuts import render
from .models import Parroquia, BarrioCiudadela
from .forms import ParroquiaForm, BarrioCiudadelaForm
from django.shortcuts import render, redirect

def lista_parroquias(request):
    """
    Listar los registros del modelo Parroquia y sus barrios asociados.
    """
    parroquias = Parroquia.objects.all()
    informacion_template = {
        'parroquias': parroquias,
        'numero_parroquias': parroquias.count()
    }
    return render(request, 'parroquiasBarrios.html', informacion_template)

def lista_barrios(request):
    """
    Listar los registros del modelo BarrioCiudadela.
    """
    barrios = BarrioCiudadela.objects.all()
    informacion_template = {
        'barrios': barrios,
        'numero_barrios': barrios.count()
    }
    return render(request, 'barrios.html', informacion_template)

def crear_parroquia(request):
    """
    Crear una nueva parroquia usando un formulario.
    """
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_parroquias')
    else:
        formulario = ParroquiaForm()
    return render(request, 'parroquias.html', {'formulario': formulario})

def crear_barrio(request):
    """
    Crear un nuevo barrio usando un formulario.
    """
    if request.method == 'POST':
        formulario = BarrioCiudadelaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_barrios')
    else:
        formulario = BarrioCiudadelaForm()
    return render(request, 'crearBarrio.html', {'formulario': formulario})

def index(request):
    """
    Vista principal del sistema mostrando conteos.
    """
    numero_parroquias = Parroquia.objects.count()
    numero_barrios = BarrioCiudadela.objects.count()
    contexto = {
        'numero_parroquias': numero_parroquias,
        'numero_barrios': numero_barrios
    }
    return render(request, 'index.html', contexto)
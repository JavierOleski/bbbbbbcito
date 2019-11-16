from django.core.files.storage import default_storage, FileSystemStorage
from django.db.models.fields.files import FieldFile
from django.shortcuts import render, redirect
from .forms import FichaForm, EjemploForm
from .models import Ficha, Example
from django.contrib.auth.forms import UserCreationForm

# http://yuji.wordpress.com/2013/01/30/django-form-field-in-initial-data-requires-a-fieldfile-instance/
class FakeField(object):
    storage = default_storage

fieldfile = FieldFile(None, FakeField, "dummy.txt")


def home(request):
    return render(request, 'home.html')

def registrarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {
        'form': form
    })

def acercade(request):
    return render(request, 'acercade.html')

def lista_pacientes(request):
    lista = Ficha.objects.all()
    return render(request, 'lista_pacientes.html', {
        'lista': lista
    })


def example_list(request):
    ejemplos = Example.objects.all()
    return render(request, 'example_list.html', {
        'ejemplos': ejemplos
    })


def ficha(request):
    if request.method == 'POST':
        form = FichaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = FichaForm()
    return render(request, 'ficha.html', {
        'form': form
    })


def example(request):
    if request.method == 'POST':
        form = EjemploForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('example_list')
    else:
        form = EjemploForm()
    return render(request, 'example.html', {
        'form': form
    })
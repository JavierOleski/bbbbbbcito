from django.core.files.storage import default_storage, FileSystemStorage
from django.db.models.fields.files import FieldFile
from django.shortcuts import render, redirect
from .forms import FichaForm
from .models import Ficha
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
    return render(request, 'lista_pacientes.html')

def ficha(request):
    form = FichaForm
    return render(request, 'ficha.html', {
        'form': form
    })


def example(request):
    if request.method == 'POST':
        myfile = request.FILES['document']
        print(myfile.name)
        print(myfile.size)
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)
    return render(request, 'example.html')

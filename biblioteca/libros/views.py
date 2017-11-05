# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from .forms import LibroModelForm
from .mixin import FormUserNeededMixin


from .models import Libro


# Create your views here.

class LibroCreateView(FormUserNeededMixin, CreateView):
    form_class = LibroModelForm
    template_name = "CrearLibro_view.html"
    success_url = "/libros/list"

class LibroUpdateView(UpdateView):
    queryset = Libro.objects.all()
    form_class = LibroModelForm
    template_name = "Actualizar_view.html"
    success_url = "/libros/list"

def home(request):
    print request
    Titulo="Libros"
    return render(request, 'home.html', {'TitleV': Titulo})

def lista_libros(request):
    result_set = Libro.objects.all()
    context = {
    "result": result_set
    }
    return render(request, "lista_libros.html", context)

def detalle_libro(request, id=1):
    result_set = Libro.objects.get(id=id)
    context = {
    "result": result_set
    }
    return render(request, "detalle_libro.html", context)

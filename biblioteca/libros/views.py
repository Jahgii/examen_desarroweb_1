# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import LibroModelForm
from .mixin import FormUserNeededMixin
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Libro


# Create your views here.

class LibroCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = LibroModelForm
    template_name = "CrearLibro_view.html"
    success_url = "/libros/list"

class LibroUpdateView(LoginRequiredMixin, UpdateView):
    queryset = Libro.objects.all()
    form_class = LibroModelForm
    template_name = "Actualizar_view.html"
    success_url = "/libros/list"

class LibroDeleteView(LoginRequiredMixin, FormUserNeededMixin, DeleteView):
    model = Libro
    template_name = "Delete_confirm.html"
    success_url = reverse_lazy("list")

class LibroListView(ListView):
    template_name = "libro_list_ajax.html"

    def get_queryset(self, *args, **kwargs):
        qs = Libro.objects.all().order_by("-pk")
        print self.request.GET
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
            Q(Nombre__icontains=query)|
            Q(Autor__icontains=query) |
            Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
         context = super(LibroListView, self).get_context_data(*args, **kwargs)
         print context
         context['create_form'] = LibroModelForm()
         context['create_url'] = reverse_lazy("Libro_create")
         return context

def home(request):
    print request
    Titulo="Libros"
    return render(request, 'home.html', {'TitleV': Titulo})

def detalle_libro(request, id=1):
    result_set = Libro.objects.get(id=id)
    context = {
    "result": result_set
    }
    return render(request, "detalle_libro.html", context)

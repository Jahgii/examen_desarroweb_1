from django import forms

from .models import Libro

class LibroModelForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = [
            #"user",
            "Nombre", "Autor", "Editorial", "ISBN",
            "precio"
            ]

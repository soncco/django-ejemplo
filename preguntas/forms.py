# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput, Textarea, SelectMultiple, HiddenInput

from .models import Pregunta, Comentario

class PreguntaForm(ModelForm):
  class Meta:
    model = Pregunta
    fields = ['titulo', 'descripcion', 'categoria']

    widgets = {
      'titulo': TextInput(attrs = {
        'class': 'form-control',
        'placeholder': 'Título',
        'required': 'required'
      }),
      'descripcion': Textarea(attrs = {
        'class': 'form-control',
        'placeholder': 'Descripción',
        'required': 'required'
      }),
      'categoria': SelectMultiple(attrs = {
        'class': 'form-control',
        'required': 'required',
      }),
    }

class ComentarioForm(ModelForm):
  class Meta:
    model = Comentario
    fields = ['contenido']

    widgets = {
      'contenido': Textarea(attrs = {
        'class': 'form-control',
        'placeholder': 'Agregue su comentario aquí',
        'required': 'required'
      }),
    }
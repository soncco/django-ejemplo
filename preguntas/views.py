# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib import messages

from .models import Categoria, Pregunta, Comentario

from .forms import PreguntaForm, ComentarioForm

def index(request):
    preguntas = Pregunta.objects.all()
    context = {'preguntas': preguntas}
    return render(request, 'index.html', context)

def categoria(request, categoria_id):
    try:
        categoria = Categoria.objects.get(pk = categoria_id)
    except Categoria.DoesNotExist:
        raise Http404
    context = {'categoria': categoria}
    return render(request, 'categoria.html', context)

def crear_pregunta_hastalas(request):
    if request.method == 'POST':
        from django.utils import timezone
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        _categorias = request.POST.getlist('categoria[]')
        fecha = timezone.now()

        pregunta = Pregunta(titulo = titulo, descripcion = descripcion, fecha = fecha)
        pregunta.save()

        for cat in _categorias:
            categoria = Categoria.objects.get(pk = cat)
            pregunta.categoria.add(categoria)

        pregunta.save()

        messages.success(request, 'Se ha creado una nueva pregunta')

    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'crear.html', context)


def crear_pregunta(request):
    form = PreguntaForm()
    if request.method == 'POST':
        form = PreguntaForm(request.POST)

        if form.is_valid():
            pregunta = form.save(commit = False)
            from django.utils import timezone
            pregunta.fecha = timezone.now()
            pregunta.save()
            form.save_m2m()
            messages.success(request, 'Se ha creado una nueva pregunta.')
        else:
            messages.error(request, 'No se pudo guardar, intente nuevamente.')

    categorias = Categoria.objects.all()
    context = {'categorias': categorias, 'form': form}
    return render(request, 'crear.html', context)

def pregunta(request, pregunta_id):
    form = ComentarioForm()
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit = False)
            comentario.pertenece_a = Pregunta.objects.get(pk = pregunta_id)
            comentario.save()

            messages.success(request, 'Se ha añadido el comentario.')

            form = ComentarioForm()

        else:
            messages.error(request, 'No se pudo guardar, intente nuevamente.')


    try:
        pregunta = Pregunta.objects.get(pk = pregunta_id)
    except Pregunta.DoesNotExist:
        raise Http404
    context = {'pregunta': pregunta, 'form': form}
    return render(request, 'pregunta.html', context)

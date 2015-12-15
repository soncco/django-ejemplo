from __future__ import unicode_literals

from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre

class Pregunta(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    categoria = models.ManyToManyField(Categoria)

    def __unicode__(self):
        return self.titulo

class Comentario(models.Model):
  contenido = models.TextField()
  pertenece_a = models.ForeignKey(Pregunta, default = None)


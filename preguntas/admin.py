from django.contrib import admin

from .models import Categoria, Pregunta, Comentario

class ComentarioInline(admin.TabularInline):
  model = Comentario

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha',)
    search_fields = ['titulo',]
    list_filter = ('fecha', 'categoria')
    inlines = [ComentarioInline,]

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('contenido', 'pertenece_a',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Comentario, ComentarioAdmin)

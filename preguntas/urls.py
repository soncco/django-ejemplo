from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',  views.index, name='index'),
    url(r'^categoria/(?P<categoria_id>.*)$',  views.categoria, name='categoria'),
    url(r'^crear$',  views.crear_pregunta, name='crear_pregunta'),
    url(r'^pregunta/(?P<pregunta_id>.*)$',  views.pregunta, name='pregunta'),
    
]

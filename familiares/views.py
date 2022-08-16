from operator import and_
from django.shortcuts import render
from django.http import HttpResponse
from familiares.models import Familiares
from django.template import Template, Context

# Create your views here.

def lista_familiares(request):
    
    familiares = Familiares.objects.all()
    lista_familiares_nombre = []

    lista_familiares_fecha_nacimiento = []

    mi_template = open(r"C:\Users\Nahuel\Desktop\MVT COLANTONIO ALEXIS NAHUEL\MVT_COLANTONIO_ALEXIS_NAHUEL\MVT_COLANTONIO_ALEXIS_NAHUEL\template\index.html", "r")

    plantilla = Template(mi_template.read())

    mi_template.close()

    context = Context()

    documento_a_devolver= plantilla.render (context)

    return HttpResponse(documento_a_devolver)



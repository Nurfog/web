from django.http import HttpResponse
from django.template import Template, Context
from jj.classes.Home import Home
from jj.settings import BASE_DIR
from django.template import loader
from django.shortcuts import render





def master(request):
    x = Home("Juan Enrique", "Allende")       
    return render(request, "master.html", {"nombre":str(x.name),"apellido":str(x.lastname)})

def index(request):
    x = Home("Juan Enrique", "Allende")       
    return render(request, "index.html", {"nombre":str(x.name),"apellido":str(x.lastname)})



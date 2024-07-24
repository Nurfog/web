from django.http import HttpResponse
from jj.classes.Home import Home




def index(request):
    x = Home("Juan", "Allende")
    return HttpResponse("Hola " + str(x))


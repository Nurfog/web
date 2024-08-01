from django.http import HttpResponse
from django.template import Template, Context
from jj.classes.Home import Home






def index(request):
    x = Home("Juan Enrique", "Allende")
    #favicon = STATIC_ROOT
    doc_externo = open('jj/templates/index.html', 'r', encoding='utf-8')
    ptl = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre":str(x.name),"apellido":str(x.lastname)})
    documento = ptl.render(ctx)    
    return HttpResponse(documento)




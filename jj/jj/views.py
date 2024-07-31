from django.http import HttpResponse
from django.template import Template, Context
from jj.classes.Home import Home





def index(request):
    x = Home("Juan Enrique", "Allende")
    #x.favicon()
    doc_externo = open('jj/templates/index.html', 'r', encoding='utf-8')
    ptl = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre":str(x)},{"xfavicon":x.favicon(x.favicon)})
    documento = ptl.render(ctx)    
    return HttpResponse(documento)




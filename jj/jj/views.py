from django.http import HttpResponse
from django.template import Template, Context
from jj.classes.Home import Home
from jj.settings import BASE_DIR, STATIC_ROOT,STATICFILES_DIRS






def index(request):
    x = Home("Juan Enrique", "Allende")
    #favicon = open('./static/admin/img/favicon.png')
    pag = BASE_DIR
    estatica = STATICFILES_DIRS
    doc_externo = open('jj/templates/index.html', 'r', encoding='utf-8')
    ptl = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre":str(x.name),"apellido":str(x.lastname),"pagina":pag, "estatica":estatica})
    documento = ptl.render(ctx)    
    return HttpResponse(documento)




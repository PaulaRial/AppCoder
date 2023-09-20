from django.http import HttpResponse
from django.template import Template, Context, loader


def test_template(request):
        datos = {"nombre" : "Pepe" , "notas" : [1,6,10,6,5,6,8,8,7,2,1,10,9]}
        plantilla = loader.get_template("template.html")
        documento = plantilla.render(datos)
        return HttpResponse(documento)

"""
def test_template(request):
    mi_html = open("C:/Users/paula/OneDrive/Escritorio/Proyecto Final/proyecto1/proyecto1/plantillas/template.html")
    
    plantilla = Template(mi_html.read())

    mi_html.close()

    mi_contexto = Context({"nombre" : "Pepe" , "notas" : [1,6,10,6,5,6,8,8,7,2,1,10,9]})

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)
"""
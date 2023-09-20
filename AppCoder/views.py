from django.shortcuts import render
from AppCoder.models import Curso, Avatar, Profesores
from django.template import loader
from django.http import HttpResponse
from AppCoder.forms import Curso_form , UserEditForm, Profesores_form
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

#def alta_curso(request, nombre, comision):
    #curso = Curso(nombre=nombre, comision=comision)
    #curso.save()
    #texto = f"Se guardo el Curso: {curso.nombre} , Comision: {curso.comision} en la BD"
    #return HttpResponse(texto)

def inicio(request):
    print(request.user.id)
    if request.user.id != None:
        avatares = Avatar.objects.filter(user=request.user.id)
        return render (request, "padre.html", {"url":avatares[0].imagen.url})
    else:
        return render (request, "padre.html")
    #return render(request, "padre.html")


def cursos(request):
    cursos = Curso.objects.all()
    #return (request, "cursos.html" , {"cursos":cursos})
    dicc = {"cursos" : cursos}
    plantillas = loader.get_template("cursos.html")
    documento = plantillas.render(dicc)
    return HttpResponse(documento)

@login_required
def profesores(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render (request, "profesores.html" , {"url":avatares[0].imagen.url})
    #return render(request, "profesores.html")

@login_required
def alumnes(request):
    print(request.user.id)
    if request.user.id != None:
        avatares = Avatar.objects.filter(user=request.user.id)
        return render (request, "alumnes.html", {"url":avatares[0].imagen.url})
    else:
        return render (request, "alumnes.html")
    #return render(request, "alumnes.html")

def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = Curso_form(request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data  
            curso= Curso(nombre= datos['nombre'], comision= datos['comision'])
            curso.save()
        return render(request, "formulario.html")
    
    return render(request, "formulario.html")


def buscar_curso(request):
    return render(request, "buscar_curso.html")

def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render(request, "resultado_busqueda.html", {"cursos":cursos})
    else:
        return HttpResponse("Campo vacio")
    

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    cursos = Curso.objects.all()
    return render(request, "cursos.html", {"cursos":cursos})


def editar(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST": 
        mi_formulario = Curso_form( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos['nombre']
            curso.comision = datos['comision']
            curso.save()
            cursos = Curso.objects.all()
            return render(request, "cursos.html", {"cursos":cursos})
    else:
        mi_formulario = Curso_form(initial={"nombre": curso.nombre , "comision":curso.comision})
    return render (request, "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})

def login_request(request):
    if request.method == "POST":
        
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            usuarie = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuarie , password=contra)
            
            if user is not None:
                login (request, user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render (request, "inicio.html" , {"url":avatares[0].imagen.url})
            else:
                return HttpResponse(f"Datos Incorrectos: intente nuevamente")
        else:
            return HttpResponse(f"FROM INCORRECTO {form}")
    
    
    form = AuthenticationForm()
    return render(request, "login.html" , {"form":form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Su cuenta se ha creado correctamente")

    else:
        form=UserCreationForm
        return render(request, "registro.html", {"form":form})
    


def editarPerfil (request):

    usuarie = request.user

    if request.method == "POST":
        
        miFormulario = UserCreationForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuarie.email = informacion['email']
            password = informacion['passoword1']
            usuarie.set_password(password)
            usuarie.save()
            return render (request, "inicio.html")
    else:
        miFormulario = UserEditForm(initial={'email': usuarie.email})
    return render (request, "editar_perfil.html", {"miFormulario":miFormulario, "usuarie":usuarie})




def about(request):
    print(request.user.id)
    if request.user.id != None:
        avatares = Avatar.objects.filter(user=request.user.id)
        return render (request, "about.html", {"url":avatares[0].imagen.url})
    else:
        return render (request, "about.html")
    
   


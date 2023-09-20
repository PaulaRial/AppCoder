from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ("", views.inicio, name="home"),
    path ("cursos", views.cursos , name="cursos"),
    #path ("alta_curso/<str:nombre>/<int:comision>" , views.alta_curso),
    path("profesores" , views.profesores , name="profesores"),
    path ("alumnes" , views.alumnes , name="alumnes"),
    path ("alta_curso", views.curso_formulario),
    path ("buscar_curso", views.buscar_curso),
    path ("buscar", views.buscar),
    path ("eliminar_curso/<int:id>", views.eliminar_curso, name="eliminar_curso"),
    path ("editar_curso/<int:id>", views.editar, name="editar_curso"),
    path ("editar_curso", views.editar, name="editar_curso"),
    path ("login", views.login_request, name="Login"),
    path ("register", views.register, name="Register"),
    path ("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path ("editarPerfil", views.editarPerfil, name="EditarPerfil"),
    path('about', views.about, name='about'),
    path('librosyprogramas', views.about, name='material'),

]

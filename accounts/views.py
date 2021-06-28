from django.shortcuts import redirect, render
from django.db import IntegrityError
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from .models import User

# Create your views here.


def index(request):
    return render(request, "usuario/index.html")


def login(request):
    # Muestra la pagina si es solicitada con un GET
    if request.method == "GET":
        return render(request, "usuario/login.html")

    # cuando un post es enviado
    else:
        # guarda los datos del usuario en variables
        username = request.POST["username"]
        password = request.POST["password"]

        # compara los datos enviados por el post con los que hay en la base de datos
        user = authenticate(request, username=username, password=password)

        # si los datos coinciden, logea al usuario y lo redirecciona al index
        if user is not None:
            login(request, user)
            return redirect("{% url 'acc:index'%}")

        # sino los manda al login (agregar mensaje de error!!!)
        else:
            return render(request, "usuario/login.html")


def logout(request):
    # cierra la sesion
    logout(request)
    return redirect("{% url 'acc:login' %}")


def register(request):
    # guarda los datos enviados a traves del post en variables
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        # checkea si la contraseña es igual a la confirmacion (agregar mensaje de error!!!)
        if password != confirmation:
            return render(request, "usuario/register.html")

        # va a intentar crear un nuevo usuario
        try:
            user = User.objects.create_user(username, email, password)
            user.save()

        # si el nombre esta en uso tira un error (agregar mensaje de error!!)
        except IntegrityError:
            return render(request, "usuario/register.html")

        # si el usuario es registrado, lo logea
        login(request, user)
        return redirect("{% url 'acc:index' %}")

    else:
        return render(request, "usuario/register.html")

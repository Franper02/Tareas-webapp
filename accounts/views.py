from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "usuario/index.html")


def login(request):
    if request.method == "GET":
        return render(request, "usuario/login.html")
    return HttpResponse("Comming soon")

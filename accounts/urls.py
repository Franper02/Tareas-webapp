from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = 'acc'

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login")
]

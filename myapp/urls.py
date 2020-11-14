from django.urls import path, include
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import ClienteCreate
from .views import RegistroUsuario, listar
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.auth.views import login_required



urlpatterns = [
    path('packs', views.packs, name="packs"),
    path('subscribir_cliente', login_required(ClienteCreate.as_view()), name="subscribir_cliente"),
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('listar', listar.as_view(), name="listar"),
    


]

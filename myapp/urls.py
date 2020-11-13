from django.urls import path, include
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import ClienteCreate


urlpatterns = [
    path('index', views.index, name="index"),
    path('packs', views.packs, name="packs"),
    path('subscripcion', views.subscripcion, name="subscripcion"),
    path('subscribir_cliente', ClienteCreate.as_view(), name="subscribir_cliente"),
]

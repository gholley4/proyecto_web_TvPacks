from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('packs', views.packs, name="packs"),
    path('subscripcion', views.subscripcion, name="subscripcion"),
]

from django.shortcuts import render, redirect
from .forms import ClienteForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import RegistroForm



# Create your views here.
def packs(request):
    return render(request, 'myapp/packs.html')

def subscripcion(request):
    return render(request, 'myapp/subscripcion.html')

class RegistroUsuario(CreateView):
    model = User
    template_name = 'myapp/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('home')


class ClienteCreate (CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'myapp/subscripcion.html'
    success_url = reverse_lazy('packs')

class listar(ListView):
    model = User
    template_name = 'myapp/listar.html'


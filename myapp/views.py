from django.shortcuts import render, redirect
from .forms import ClienteForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente



# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def packs(request):
    return render(request, 'myapp/packs.html')

def subscripcion(request):
    return render(request, 'myapp/subscripcion.html')

class ClienteCreate (CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'myapp/subscripcion.html'
    success_url = reverse_lazy('packs')

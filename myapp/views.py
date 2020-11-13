from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def packs(request):
    return render(request, 'myapp/packs.html')

def subscripcion(request):
    return render(request, 'myapp/subscripcion.html')
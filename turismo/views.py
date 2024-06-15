from django.shortcuts import render
from .models import Servicios
# Create your views here.
def index(request):
    context={}
    return render(request, 'turismo/index.html', context)

def listar(request):
    servicios = Servicios.objects.all()
    return render(request, 'turismo/listar.html', {'servicios': servicios})
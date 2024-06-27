from django.shortcuts import render,redirect,get_object_or_404 
from .models import Servicios
from .forms import ServiciosForm
# Create your views here.
def index(request):
    context={}
    return render(request, 'turismo/index.html', context)

def listar(request):
    servicios = Servicios.objects.all()
    return render(request, 'turismo/listar.html', {'servicios': servicios})

def editar(request, servicio_id):
    servicio = get_object_or_404(Servicios, id_servicio=servicio_id)
    if request.method == 'POST':
        form = ServiciosForm(request.POST, request.FILES, instance=servicio)  # Añade request.FILES aquí
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = ServiciosForm(instance=servicio)
    return render(request, 'editar.html', {'form': form})
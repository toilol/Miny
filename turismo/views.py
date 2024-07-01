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
    servicios = get_object_or_404(Servicios, id_servicio=servicio_id)
    if request.method == 'POST':
        form = ServiciosForm(request.POST, request.FILES, instance=servicios)  # Añade request.FILES aquí
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = ServiciosForm(instance=servicios)
    return render(request, 'turismo/editar.html', {'form': form})

def agregar(request):
    if request.method == 'POST':
        form = ServiciosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = ServiciosForm()
    return render(request, 'turismo/agregar.html', {'form': form})

def borrar(request,pk):
    context={}
    try:
        servicio = Servicios.objects.get(id_servicio=pk)
        servicio.delete()
        mensaje= "datos eliminados"
        servicio = Servicios.objects.all()
        context = {'servicios': servicios, 'mensaje': mensaje}
    except:
        mensaje= "error, el servicio no existe"
        servicio = Servicios.objects.all()
        context = {'servicios': servicios, 'mensaje': mensaje}
        return render(request, 'turismo/listar.html', context)

def carrito(request):
    servicio_id = request.POST.get('servicio_id')  # suponiendo que obtienes el id del servicio
    servicio = Servicios.objects.get(id_servicio=servicio_id)
    
    cart = request.session.get('cart', [])
    cart.append({
        'descripcion': servicio.descripcion,
        'precio': float(servicio.precio),  # asegúrate de convertir el precio a float
    })
    request.session['cart'] = cart
    
    return HttpResponseRedirect(reverse('carrito'))  # redirecciona a la página del carrito


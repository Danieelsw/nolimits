from django.shortcuts import render
from .models import Producto

# Create your views here.

def mostrarIndex(request):
    return render(request,"index.html") 

def mostrarRegistro(request):
    return render(request, "registros.html")

def mostrarListado(request):
    pro = Producto.objects.all().values()
    datos = {
        'pro':pro
    }
    return render(request, "listado.html", datos)

def mostrarCatalogo(request):
    pro = Producto.objects.all().values()
    datos = {
        'pro':pro
    }
    return render(request, "catalogo.html", datos)


def registrarProducto(request):
    if request.method == 'POST':
        tit = request.POST['txttit']
        pre = request.POST['txtpre']

        try:
            fot = request.FILES['txtfot']
        except:
            fot = "imagen_bd/no_imagen.png"

        pro = Producto(nombre=tit, precio=pre, foto=fot)
        pro.save() 
        datos={'r' : 'Producto agregado correctamente'}
        return render(request,'registros.html', datos)
    
    else:
        datos = {'r2':'No se puede agregar el producto'}
        return render(request,'registros.html',datos)
    
def eliminarProducto(request,id):
    try:
        pro = Producto.objects.get(id=id)
        pro.delete()
        pro = Producto.objects.all().values()
        datos = {
            'pro': pro,
            'r':'El producto fue eliminado'
        }
        return render(request,"listado.html",datos)
    except:
        pro = Producto.objects.all().values()
        datos = {
            'pro': pro,
            'r':'No existe el producto'
        }
        return render(request,"listado.html",datos)

def actualizarProducto(request,id):
    try:
        pass
    except:
        pass

        




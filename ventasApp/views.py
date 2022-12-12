from django.shortcuts import render, HttpResponse
from ventasApp.models import Persona, Colaborador, Producto, Boleta, DetalleBoleta, Venta
import random

# Create your views here.

def index(request):
    return render(request, 'menu.html')

def venta(request):
    
    # Mostrar todos los productos
    products = Producto.objects.order_by('id')
    #products = Producto.objects.raw("SELECT * FROM ventasapp_producto ORDER BY id")
    
    return render(request, 'ventas.html', {
        'products': products
    })

def registroUsuario(request):    
    return render(request, 'registro.html')

def verVentas(request):
    
    ventas = Venta.objects.order_by('id')
    
    return render(request, 'verVentas.html', {
        'ventas': ventas
    })

def save(request):
    
    if request.method == 'POST':
        # PERSONA
        rut = request.POST['dni']
        nombre = request.POST['firstName']
        apellido_paterno = request.POST['lastName1']
        apellido_materno = request.POST['lastName2']
        email = request.POST['email']
        direccion = request.POST['address']
        ciudad = request.POST['address1']
        
        # COLABORADOR
        cargo = request.POST['position']  
        contrasena = request.POST['password']
        tipo_contrato = request.POST['contract']
        jefe_directo = request.POST['boss']
        
        persona = Persona(
            rut = rut,      
            nombre = nombre,
            apellido_paterno = apellido_paterno,
            apellido_materno = apellido_materno,
            email = email,
            direccion = direccion,
            ciudad = ciudad
        )
        persona.save() # Guarda el dato en la BBDD
        
        colaborador = Colaborador(
            cargo = cargo,
            contrasena = contrasena,
            tipo_contrato = tipo_contrato,
            jefe_directo = jefe_directo
        )
        colaborador.save() # Guarda el dato en la BBDD
        
        return render(request, 'menu.html')

def sell(request):
    if request.method == 'POST':
        
        metodo_pago = request.POST['metodo_de_pago']
        
        nombre = request.POST['productName']
        precio = request.POST['price']
        codigo_producto = request.POST['codigo']
        
        vender = Venta(
            nombre = nombre,
            precio = precio,
            codigo_producto = codigo_producto,
            metodo_pago = metodo_pago,
            precio_total = float(precio) * 1.19,
            iva = 19,
            numero_boleta = int(random.randrange(9))
        )        
        vender.save()
        
        return render(request, 'menu.html')
from django.shortcuts import render, HttpResponse
from ventasApp.models import Persona, Colaborador, Producto, Boleta, DetalleBoleta, Venta

# Create your views here.

def index(request):
    return render(request, 'index.html')

def venta(request):
    
    
    # Mostrar todos los productos
    products = Producto.objects.order_by('id')
    #products = Producto.objects.raw("SELECT * FROM ventasapp_producto ORDER BY id")
    
    return render(request, 'venta.html', {
        'products': products
    })

def registroUsuario(request):
    
    if request.method == 'GET':
        
        # PERSONA
        nombre = request.GET['nombre']
        apellido_paterno = request.GET['apPaterno']
        apellido_materno = request.GET['apMaterno']
        rut = request.GET['rut']
        direccion = request.GET['direccion']
        ciudad = request.GET['ciudad']
        telefono = request.GET['numTelefono']
        email = request.GET['email']
        
        # COLABORADOR
        contrasena = request.GET['contras']
        cargo = request.GET['cargo']
        tipo_contrato = request.GET['tipoContrato']
        jefe_directo = request.GET['jefeDirecto']
        
        persona = Persona(            
            name = nombre,
            lastName1 = apellido_paterno,
            lastName2 = apellido_materno,
            dni = rut,
            address = direccion,
            city = ciudad,
            phone = telefono,
            email = email
        )
        persona.save() # Guarda el dato en la BBDD
        
        colaborador = Colaborador(
            password = contrasena,
            position = cargo,
            contract = tipo_contrato,
            boss = jefe_directo
        )
        colaborador.save() # Guarda el dato en la BBDD
        
        
        
        return render(request, 'registro.html')
    
    else:
        return HttpResponse("<h2>No se ha creado ningun usuario</h2>")
    
    
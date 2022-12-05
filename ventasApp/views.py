from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def venta(request):
    return render(request, 'venta.html')

def registroUsuario(request):
    return render(request, 'registro.html')
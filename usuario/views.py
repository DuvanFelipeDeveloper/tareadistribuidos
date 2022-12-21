from django.shortcuts import render
from .models import Producto 

# Create your views here.

def home(request):
    productoslistados =Producto.objects.all()
    return render(request,"lista.html", {"productos": productoslistados})

from django.shortcuts import render
from .models import Producto 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests



# Create your views here.

def home(request):

    url = "https://drive.google.com/uc?id=1OuUHXjkP-Si-F8IaynyCebgIRsHDRgKH&export=download&authuser=0"

    response= requests.get(url)

    print(response.text)
    
    productoslistados =Producto.objects.all()
    return render(request,"lista.html", {"productos": productoslistados, "titulo": response.text})
    
    

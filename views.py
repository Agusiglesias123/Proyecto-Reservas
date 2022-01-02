from django.shortcuts import render

from .forms import Solicitud
from .models import Reserva

# Create your views here.

def index(request):

    return render(request, "index.html")

def login(request):

    return render(request, "login.html")


def gestion(request):
    reserva= Reserva.objects.all()
    return render(request,'gestion.html',{'reserva':reserva})

def galeria(request):
    if request.method == 'POST':
        form= Solicitud(request.POST)
        if form.is_valid():
            form.save()
            form = Solicitud()
    else:
        form = Solicitud()
    return render(request, 'galeria.html', {'form':form})

def eliminar(request, id_reserva):
    reserva = Reserva.objects.get(pk=id_reserva)
    reserva.delete()
    reserva = Reserva.objects.all()
    return render(request,'gestion.html',{'reserva':reserva})

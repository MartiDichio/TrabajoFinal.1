
from django.shortcuts import render, get_object_or_404, redirect
from .models import Avance, Contacto
from django.urls import reverse

def avance_list(request):
    avances = Avance.objects.all()
    return render(request, 'silicon/avance_list.html', {'avances': avances}) ##aca tenemos vista del listado

def avance_detail(request, pk):
    avance = get_object_or_404(Avance, pk=pk)
    return render(request, 'silicon/avance_detail.html', {'avance': avance})  ##aca vista de los detalles


def avance_create(request):
    if request.method == 'POST':
        descripcion = request.POST['descripcion']
        progreso = request.POST['progreso']
        fecha = request.POST['fecha']
        Avance.objects.create(descripcion=descripcion, progreso=progreso, fecha=fecha)## aca esta para crear
        return redirect(reverse('avance_list'))
    return render(request, 'silicon/avance_form.html')


def avance_delete(request, pk):
    avance = get_object_or_404(Avance, pk=pk)
    if request.method == 'POST':
        avance.delete()
        return redirect(reverse('avance_list')) ## aca se elimina
    return render(request, 'silicon/avance_confirm_delete.html', {'avance': avance})

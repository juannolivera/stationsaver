from django.shortcuts import render, redirect, get_object_or_404
from .models import Surtidor, Transaccion

def cargar_combustible(request):
    if request.method == 'POST':
        # Procesa los datos del formulario y crea la transacción
        surtidor_id = request.POST['surtidor']
        cantidad = request.POST['cantidad']

        surtidor = Surtidor.objects.get(pk=surtidor_id)
        precio = surtidor.precio_por_litro * cantidad
        transaccion = Transaccion.objects.create(surtidor=surtidor, cantidad=cantidad)

        # Redirige al usuario a la página de "Ticket" y pasa los datos como argumentos en la URL
        return redirect('generar_ticket', transaccion_id=transaccion.id)

    else:
        surtidores = Surtidor.objects.all()
        return render(request, 'cargar_combustible.html', {'surtidores': surtidores})

def generar_ticket(request, transaccion_id):
    # Obtén la transacción correspondiente o devuelve un error 404 si no existe
    transaccion = get_object_or_404(Transaccion, pk=transaccion_id)

    # Renderiza un template de ticket y pasa los datos de la transacción
    return render(request, 'ticket.html', {'transaccion': transaccion})

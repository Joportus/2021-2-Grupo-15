from django.shortcuts import render, redirect
from django.http import HttpResponse
from wallet.fwallet.models import RegistroDinero

# Create your views here.
def walletv(request):

    dict = {"ingresos":"ingresos", "gastos": "gastos"}
    return render(request, "fwallet\wallet.html", dict)

#Busca un registro de ingreso/gasto filtrando por el monto
def buscar(request):
    input1_name = "monto"

    pagina_resultado = "resultados_busq_monto.html"

    if request.GET[input1_name]:

        monto_ingresado = request.GET["monto_ingresado"]
        registro = RegistroDinero.objects.filter(monto__icontrains=monto_ingresado)

        return render(request, pagina_resultado, {"registro":registro, "query":monto_ingresado})

    else:

        mensaje = "No se introdujo nada"

    return HttpResponse(mensaje)



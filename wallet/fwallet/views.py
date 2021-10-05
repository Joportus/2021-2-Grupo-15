from django.shortcuts import render, redirect
from django.http import HttpResponse
from fwallet.models import RegistroDinero

# Create your views here.
def walletv(request):

    dict = {"ingresos":"ingresos", "gastos": "gastos"}
    return render(request, "fwallet\wallet.html", dict)


def busqueda_registros(request):
    return render(request, "fwallet/busqueda_registros.html")

def insertar_registros(request):
    return render(request, "fwallet/insertar_registro.html")

def inicio(request):

    return render(request, "fwallet/inicio.html")

#Busca un registro de ingreso/gasto filtrando algun parámetro
def filtrar_por(request):
    input1_name = "reg"
    input2_name = "reg2"
    input3_name = "all_reg"
    input4_name = "reg3"
    input5_name = "reg4"
    input6_name = "reg5"

    pagina_resultado = "fwallet/busqueda_registros.html"

    if request.POST.get(input1_name):

        monto_ingresado = request.POST.get(input1_name)
        registros = RegistroDinero.objects.filter(monto__iexact=monto_ingresado)

        return render(request, pagina_resultado, {"registros":registros, "query":monto_ingresado})


    elif request.POST.get(input2_name):

        fecha_ingresada = request.POST.get(input2_name)
        registros = RegistroDinero.objects.filter(fecha__iexact=fecha_ingresada)

        return render(request, pagina_resultado, {"registros":registros, "query":fecha_ingresada})


    elif request.POST.get(input3_name):

       registros = RegistroDinero.objects.all()

       return render(request, pagina_resultado, {"registros":registros})


    elif request.POST.get(input4_name):

        tipo_ingresado = "ingreso"
        registros = RegistroDinero.objects.filter(tipo__iexact=tipo_ingresado)

        return render(request, pagina_resultado, {"registros":registros, "query":tipo_ingresado})

    elif request.POST.get(input5_name):

        tipo_ingresado = "gasto"
        registros = RegistroDinero.objects.filter(tipo__iexact=tipo_ingresado)

        return render(request, pagina_resultado, {"registros":registros, "query":tipo_ingresado})

    elif request.POST.get(input6_name):

        tipo_ingresado = "deuda"
        registros = RegistroDinero.objects.filter(tipo__iexact=tipo_ingresado)

        return render(request, pagina_resultado, {"registros":registros, "query":tipo_ingresado})



    else:

        return render(request, pagina_resultado)


 
def ingresar_registro(request):
    tipo = request.POST.get("tipo")
    monto = request.POST.get("monto")
    fecha = request.POST.get("fecha")
    clase = request.POST.get("categoria")
    descripcion = request.POST.get("descripcion")
    nombre = request.POST.get("nombre")

    o_ref=RegistroDinero(tipo=tipo, monto=monto, nombre=nombre,fecha=fecha, clase = clase, descripcion=descripcion)
    o_ref.save()

    return render(request, 'fwallet/insertar_registro.html', {"message": "registrado!"})




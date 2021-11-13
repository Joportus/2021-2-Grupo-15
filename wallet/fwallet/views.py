from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from fwallet.models import RegistroDinero,User
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def walletv(request):

    dict = {"ingresos":"ingresos", "gastos": "gastos"}
    return render(request, "fwallet\wallet.html", dict)

def insertar_registros(request):
    return render(request, "fwallet/insertar_registro.html")

def inicio(request):

    return render(request, "fwallet/inicio.html")

#Busca un registro de ingreso/gasto filtrando algun parámetro
def filtrar_por(request):

    if request.user.is_authenticated:
        registros = RegistroDinero.objects.filter(owner=request.user)# quering all todos with the object manager
    else:
        registros = RegistroDinero.objects.filter(owner=None)
    input1_name = "reg"
    input2_name = "reg2"
    input3_name = "all_reg"
    input4_name = "reg3"
    input5_name = "reg4"
    input6_name = "reg5"
    input7_name = "reg6"

    pagina_resultado = "fwallet/busqueda_registros.html"

    query_filters = [0,0,0,0,0,0]

    if request.method == "GET" or request.POST.get(input3_name):


       return render(request, pagina_resultado, {"registros":registros})

    if request.POST.get(input1_name):


        monto_ingresado = request.POST.get(input1_name)
        query_filters[0] = monto_ingresado
        #registros = registros.filter(monto__iexact=monto_ingresado)

        #return render(request, pagina_resultado, {"registros":registros, "query":monto_ingresado})


    if request.POST.get(input2_name):

        fecha_ingresada = request.POST.get(input2_name)
        query_filters[1] = fecha_ingresada
        #registros = registros.filter(fecha__iexact=fecha_ingresada)

        #return render(request, pagina_resultado, {"registros":registros, "query":fecha_ingresada})


    if request.POST.get(input6_name):

        tipo_ingresado = ""
        
        if request.POST.get(input6_name) == "Deudas":
            tipo_ingresado = "deuda"
        query_filters[2] = tipo_ingresado
        #registros = registros.filter(tipo__iexact=tipo_ingresado)

        #return render(request, pagina_resultado, {"registros":registros, "query":tipo_ingresado})

    if request.POST.get(input5_name):

        tipo_ingresado = ""
        print(request.POST.get(input5_name))
        if request.POST.get(input5_name) == "Gastos":
            tipo_ingresado = "gasto"
        
        query_filters[3] = tipo_ingresado
        #registros = registros.filter(tipo__iexact=tipo_ingresado)

        #return render(request, pagina_resultado, {"registros":registros, "query":tipo_ingresado})

    if request.POST.get(input4_name):

        tipo_ingresado = ""
        print(request.POST.get(input4_name))
        if request.POST.get(input4_name) == "Ingresos":
            tipo_ingresado = "ingreso"
        query_filters[4] = tipo_ingresado
        #registros = registros.filter(tipo__iexact=tipo_ingresado)

    if request.POST.get(input7_name):
        categoria_ingresada = request.POST.get(input7_name)
        query_filters[5] = categoria_ingresada

    #return render(request, pagina_resultado, {"registros":registros})
    if query_filters[0] != 0:
        registros = registros.filter(monto__iexact=query_filters[0])
    if query_filters[1] != 0:
        registros = registros.filter(fecha__iexact=query_filters[1])
    if query_filters[2] != 0:
        registros = registros.filter(tipo__iexact=query_filters[2])
    if query_filters[3] != 0:
        registros = registros.filter(tipo__iexact=query_filters[3])
    if query_filters[4] != 0:
        registros = registros.filter(tipo__iexact=query_filters[4])
    if query_filters[5] != 0:
        registros = registros.filter(clase__iexact=query_filters[5])

    print(query_filters)
 
    return render(request, pagina_resultado, {"registros":registros})
    


 
def ingresar_registro(request):
    if request.method == "POST":  # revisar si el método de la request es POST
        tipo = request.POST.get("tipo")
        monto = request.POST.get("monto")
        fecha = request.POST.get("fecha")
        clase = request.POST.get("categoria")
        descripcion = request.POST.get("descripcion")
        nombre = request.POST.get("nombre")

        #Verificar si el usuario inició sesión o no!!
        if request.user.is_authenticated:
            o_ref = RegistroDinero(tipo=tipo, monto=monto, nombre=nombre,fecha=fecha, clase = clase, descripcion=descripcion,owner=request.user)  # Crear el usuario
        else:
            o_ref = RegistroDinero(tipo=tipo, monto=monto, nombre=nombre,fecha=fecha, clase = clase, descripcion=descripcion)
        o_ref.save()  # guardar la tarea en la base de datos.
        return render(request, 'fwallet/insertar_registro.html', {"message": "registrado!"})


def register_user(request):
    if request.method == 'GET': #Si estamos cargando la página
     return render(request, "fwallet/register_user.html") #Mostrar el template

    elif request.method == 'POST': #Si estamos recibiendo el form de registro
     #Tomar los elementos del formulario que vienen en request.POST
     nombre = request.POST['nombre']
     contraseña = request.POST['contraseña']
     mail = request.POST['mail']
     apodo = request.POST['apodo']
     genero = request.POST['genero']
     

    #Si ya existe el username
    if User.objects.filter(username=nombre).exists():
        error = "error"
        return render(request,"fwallet/register_user.html", {"error":error})
    #Crear el nuevo usuario   
    else:
        user = User.objects.create_user(username=nombre, password=contraseña, email=mail, apodo=apodo, genero=genero)

        #Redireccionar la página /inicio
        return HttpResponseRedirect('/')
    #return render(request,"fwallet/register_user.html")


def login_user(request):
    if request.method == 'GET':
        return render(request,"fwallet/login.html")
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['contraseña']
        usuario = authenticate(username=username,password=contraseña)
        if usuario is not None:
            login(request,usuario)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/register')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
from django.shortcuts import render, redirect



# Create your views here.
def walletv(request):

    dict = {"ingresos":"ingresos", "gastos": "gastos"}
    return render(request, "fwallet\index.html", dict)
    
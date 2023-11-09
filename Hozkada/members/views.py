from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

from HozkadaBokatak.models import Bezeroa

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("Errore bat egon da erabiltzailea sartzerakoan, saiatu berriro..."))
            return redirect('login')

    
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('index')

# def register_user(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data["izena"]
#             password = form.cleaned_data["pasahitza"]
#             user = authenticate(username = username, password = password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'authenticate/register_user.html', {'form':form})

def register_bezeroa(request):
    return render(request, 'register_user.html')

def register_bezeroa_erregistroa(request):
    nan = request.POST['nan']
    izena = request.POST['izena']
    abizena = request.POST['abizena']
    abizena2 = request.POST['abizena2']
    telefonoa = request.POST['telefonoa']
    emaila = request.POST['email']
    helbidea = request.POST['helbidea']
    postakodea = request.POST['pk']

    bezeroa = Bezeroa(nan=nan,
                    izena=izena,
                    abizena=abizena,
                    abizena2=abizena2,
                    telefonoa=telefonoa,
                    emaila=emaila,
                    helbidea=helbidea,
                    postakodea=postakodea)
    bezeroa.save()
    return HttpResponseRedirect(reverse('index'))
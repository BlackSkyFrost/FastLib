from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import FormLoginPersonalizado, FormRegistroPersonalizado
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def inicio(request):
    return render(request, 'fastlib/inicio.html')

def login_view(request):
    if request.method == 'POST':
        form = FormLoginPersonalizado(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('inicio')
    else:
        form = FormLoginPersonalizado()
    return render(request, 'fastlib/login.html', {'form': form})

def registro_view(request):
    if request.method == 'POST':
        form = FormRegistroPersonalizado(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FormRegistroPersonalizado()
    return render(request, 'fastlib/registro.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
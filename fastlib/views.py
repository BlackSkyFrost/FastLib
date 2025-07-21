from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import FormLoginPersonalizado, FormRegistroPersonalizado
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
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
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = FormRegistroPersonalizado()
    return render(request, 'fastlib/registro.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión.')
    return redirect('login')

@login_required
def editar_perfil_view(request):
    return render(request, 'fastlib/editar_pefil.html')

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'fastlib/cambiar_contraseña.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        messages.success(self.request, 'Contraseña cambiada con exito.')
        return super().form_valid(form)
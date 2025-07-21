from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import MyPasswordChangeView
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),
]
urlpatterns += [
    path('editar-perfil/', views.editar_perfil_view, name='editar_perfil'),
    path('cambiar-contraseña/', MyPasswordChangeView.as_view(), name='cambiar_contraseña'),
]
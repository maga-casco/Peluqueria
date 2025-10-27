from django.contrib import admin
from django.urls import path
from django.shortcuts import render

#Views de la applications
from applications.views import lista_clientes, lista_empleados, lista_servicios, lista_turnos, datos_personales 
from applications.views import register, logout_request, login_request
from applications.views import coloracion,corte,tratamiento

from django.contrib.auth import views as auth_views

def home(request):
    return render(request, "index/index.html")




###############



urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', home, name='home'),

    # Login y Registro
    path('logout/', logout_request, name= 'logout'),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),

    # Apps
    path('empleados/', lista_empleados, name='lista_empleados'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('servicios/', lista_servicios, name='lista_servicios'),
    path('turnos/', lista_turnos, name='lista_turnos'),
    
    path('coloracion/',coloracion, name='coloracion'),
    path('corte/',corte, name='corte'),
    path('tratamiento/',tratamiento, name='tratamiento'),
    
    
    #Datos Personales
    path('datos_personales/', datos_personales, name='datos_personales'),
    
    # Recuperar contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='login/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'), name='password_reset_complete'),
    
    
    
]
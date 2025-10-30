from django.shortcuts import render

#---------------------------------- LOGIN y demas en uso ----------------------------------
#from del registro
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
##para poner mensajes
from django.contrib import messages
##
from .forms import CustomUserCreationForm
from django.shortcuts import redirect


##############################################################################
# VIEWS DE LA APLICACIONES
##############################################################################
from .models import Cliente, Empleado, Servicios, Turnos

# -------------------------------------------
# LISTAS
# -------------------------------------------

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': clientes})

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista_empleados.html', {'empleados': empleados})

def lista_servicios(request):
    servicios = Servicios.objects.all()
    return render(request, 'servicios/servicios.html', {'servicios': servicios})

def lista_turnos(request):
    turnos = Turnos.objects.all()
    return render(request, 'turnos/turnos.html', {'turnos': turnos})

def coloracion (request):
    return render(request, 'coloracion/coloracion.html')

def corte (request):
    return render(request, 'corte/corte.html')

def tratamiento (request):
    return render(request, 'tratamiento/tratamiento.html')

def home(request):
    return render(request, "index/index.html")

def datos_personales(request):
    usuario = request.user
    perfil = None
    if usuario.is_cliente:
        perfil = getattr(usuario, 'cliente', None)
    elif usuario.is_empleado:
        perfil = getattr(usuario, 'empleado', None)
    return render(request, 'includes/datos_personales.html', {'usuario': usuario, 'perfil': perfil})

##############################################################################


#---------------------------------- LOGIN y demas en uso ----------------------------------
# -------------------------------------------
# REGISTRO
# -------------------------------------------

def register(request):
    #
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)   #uarda el usuario 
            # Todo registro desde la web será Cliente
            usuario.is_cliente = True
            usuario.is_empleado = False
            usuario.save()  # Dispara la señal y crea Cliente automáticamente

            messages.success(request, f'Cuenta creada para: {usuario.get_full_name()} (Cliente)')
            login(request, usuario)
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro/registro.html', {"form": form})

# -------------------------------------------
### LOGIN 
# -------------------------------------------

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Esto obtiene el usuario validado por AuthenticationForm
            login(request, user)
            messages.success(request, f'Bienvenido {user.get_full_name()}')
            return redirect('home')
        else:
            # Si form no es válido, muestra error
            messages.error(request, 'Usuario o contraseña incorrecta')
    else:
        form = AuthenticationForm() # Esto es para que aparezca el formulario vacio
    return render(request, 'login/Login.html', {'form': form})

# -------------------------------------------
### LOGOUT
# -------------------------------------------
def logout_request(request):
    logout(request)
    list(messages.get_messages(request))
    return redirect('home')

#---------------------------------- LOGIN y demas en uso ----------------------------------#

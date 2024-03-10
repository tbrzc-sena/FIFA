from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import redirect
from base.forms import CustomUserCreationForm
from django.contrib.auth import logout


def index(request):
    return render(request, 'index.html',{

    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('admin:index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'login.html',{

    })

def register_view(request):
    data ={
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        form = CustomUserCreationForm(data = request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username = form.cleaned_data["username"], password = form.cleaned_data["password1"])
            if user:
                login(request, user)
                messages.success(request, 'Usuario creado exitosamente')
                return redirect('login_view')
            else:
                data["form"] = form
    return render(request, 'register.html',data)


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login_view')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from django.views.decorators.csrf import csrf_protect
from .models import User, Post, Commentary

userCurrent=""

# Create your views here.
def Publicaciones(request):
    if request.method == 'POST':
        print(request.POST['ask'])
        user = User.objects.get(username = userCurrent)

        publicacion= Post(consult= request.POST['ask'], userid= user)
        publicacion.save()
        return redirect('/aplicacion/post/')
    else :
        print(userCurrent)
        if User.objects.filter(username = userCurrent).exists() :
            posts = Post.objects.all()
            return render(request, 'aplicacion/menu.html',{'post':posts})
        else:
            return redirect('/aplicacion/inicio/')


@csrf_protect
def HolaMundo(request):
    global userCurrent
    if request.method == 'POST':
        userCurrent= request.POST['username']
        print(userCurrent)
        return redirect('/aplicacion/post/')
    else:
        return render(request, 'aplicacion/index.html')

@csrf_protect
def CrearCuenta(request):
    if request.method == 'POST':
        user = UserForm(request.POST)
        if user.is_valid():
            print(user)
            user.save()
            return redirect('/aplicacion/inicio/')
    else:
        return render(request, 'aplicacion/crearCuenta.html')



    
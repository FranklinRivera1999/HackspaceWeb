from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from django.views.decorators.csrf import csrf_protect
from .models import User, Post, Commentary
import hashlib,os, uuid
from collections import Counter

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
            comentarios = Commentary.objects.all()
            posts = Post.objects.all()
            
            return render(request, 'aplicacion/menu.html',{'post':posts, 'comentarios': comentarios})
        else:
            return redirect('/aplicacion/inicio/')


@csrf_protect
def HolaMundo(request):
    global userCurrent
    if request.method == 'POST':
        userCurrent= request.POST['username']
        username = request.POST.get('username')
        password = request.POST.get('password')
        if comparar(username, password) :
            return redirect('/aplicacion/post/')
        else:
            return redirect('/aplicacion/inicio/')
    else:
        return render(request, 'aplicacion/index.html')

@csrf_protect
def CrearCuenta(request):
    if request.method == 'POST':
        user2 = UserForm(request.POST)
        user = User(correo = request.POST['correo'], username = request.POST['username'])
        user.password = hash_password(request.POST['password'])
        print(Counter(user.password))
        if user2.is_valid():
            user.save()
            return redirect('/aplicacion/inicio/')
    else:
        return render(request, 'aplicacion/crearCuenta.html')

def addComent(request):
    if request.method == 'POST':
        Publlicacion = Post.objects.get(id = request.POST['post'])
        comentario= Commentary(content = request.POST['coment'], postid = Publlicacion)
        comentario.save()
        return redirect('/aplicacion/post/')
    else:
        return  HttpResponse('GAAA')
    
def myPosts(request):
    if request.method == 'POST':
        post = Post.objects.get(id = request.POST['post'])
        print(post)
        post.delete()
        return redirect('/aplicacion/mispublicaciones/')
    else:
        print(userCurrent)
        if User.objects.filter(username = userCurrent).exists() :
            user = User.objects.get(username = userCurrent)
            posts = Post.objects.filter(userid= user)
            return render(request, 'aplicacion/misPublicaciones.html',{'post':posts})

        else:
            return redirect('/aplicacion/inicio/')

def editQuestion(request):
    if request.method == 'POST':
        print(request.POST['consult'])
        post =Post.objects.get(id = request.POST['post'])
        post.consult =request.POST['consult']
        post.save()
        return  redirect('/aplicacion/mispublicaciones/')
        
    
def encriptar(password):
    password_salt = os.urandom(32).hex()
    hash = hashlib.sha512()
    hash.update(('%s%s' % (password_salt, password)).encode('utf-8'))
    return hash.hexdigest()

def comparar(username2, password):
    
    if User.objects.filter(username = username2).exists() :
        passwordopcional = User.objects.get(username = username2)
        if check_password(passwordopcional.password, password) :
            return True
        else:
            return False
    else:
        return False


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
from django.shortcuts import render,redirect
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = userform()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = userdata.objects.filter(email=username, password=password)

        if user:
            messages.success(request, "Login Successfully!")
            request.session['user']=username
            return redirect('/')
        else:
            messages.error(request, "Error! Login failed...")
        
    return render(request,'login.html')


def home(request):
    return render(request,'home.html')

def logout_user(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('/')

def cart(request):
    if not request.session.get("user"):
        return redirect('login')
    
    return render(request, 'cart.html')

def add_to_cart(request):
    if not request.session.get("user"):
        return redirect('login')  
    return redirect('cart') 
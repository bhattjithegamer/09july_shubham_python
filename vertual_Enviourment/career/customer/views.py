from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=user_register.objects.filter(email=email,password=password).first()

        if user:
            request.session['user_id']=user.id
            return redirect('home')
        else:
            print("login fail")
            
    return render(request,'login.html')

def register(request):
    msg=""
    if request.method=='POST':

        email=request.POST.get('email')

        if user_register.objects.filter(email=email).exists():
            msg = "plese login"
            return render(request, 'register.html', {'msg': msg})

        form = register_form(request.POST)
        if form.is_valid():
            user=form.save()
            request.session['user_id']=user.id
            print('registered')
            return redirect('login')
        else:
            print(form.errors)
    return render(request,'register.html')

def manage_profile(request):
    user_id=request.session.get('user_id')
    if not user_id:               # session empty છે → login page redirect
        return redirect('login')
    try:
        user=user_register.objects.get(id=user_id)
    except user_register.DoesNotExist:
        return redirect('login') 
    return render(request,'manage_profile.html',{'user':user})

def search_artist(request):
    return render(request,'search_artist.html')

def book_artist(request):
    return render(request,'book_artist.html')

def cancel_booking(request):
    return render(request,'cancel_booking.html')

def feedback(request):
    return render(request,'feedback.html')

def manage_booking(request):
    return render(request,'manage_booking.html')

def userlogout(request):
    logout(request)
    return redirect('/')
from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def artist_home(request):
    return render(request,'artist_home.html')

def artist_register(request):
    msg=""
    if request.method=='POST':

        email=request.POST.get('email')

        if register_artist.objects.filter(email=email).exists():
            msg="plese login"
            return render(request,'artist_register.html',{'msg':msg})
        
        form = artist_form(request.POST)       
        if form.is_valid():
            user=form.save()
            request.session['user_id']=user.id
            print('artist done')
            return redirect('artist_login')
        else:
            print(form.errors)
    return render(request,'artist_register.html')

def artist_login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=register_artist.objects.filter(email=email,password=password).first()
        if user:
            request.session['user_id']=user.id
            return redirect('artist_home')
        else:
            print("login failed")
    return render(request,'artist_login.html')


def artist_manage_profile(request):
    user_id=request.session.get('user_id')
    if not user_id:               # session empty છે → login page redirect
        return redirect('login')
    try:
        user=register_artist.objects.get(id=user_id)
    except register_artist.DoesNotExist:
        return redirect('login') 
    return render(request,'artist_manage_profile.html',{'user':user})

def artist_upload_media(request):
    return render(request,'artist_upload_media.html')

def artist_feedback(request):
    return render(request,'artist_feedback.html')

def artist_view_feedback(request):
    return render(request,'artist_view_feedback.html')

def artist_cancel_booking(request):
    return render(request,'artist_cancel_booking.html')
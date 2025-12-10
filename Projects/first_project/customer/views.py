from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from artist.models import *
from artist.forms import *
# Create your views here.

def home(request):
    artist_files = file_artist.objects.all()
    return render(request,'home.html',{'artist_files':artist_files})

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
    msg=""
    user_id=request.session.get('user_id')
    if not user_id:               # session empty છે → login page redirect
        return redirect('login')
    try:
        user=user_register.objects.get(id=user_id)
    except user_register.DoesNotExist:
        return redirect('login') 
    if request.method=='POST':
        update_profile=register_form(request.POST,instance=user)
        if update_profile.is_valid():
            update_profile.save()
            msg="Profile Updated Successfully!"
        else:
            msg=update_profile.errors
    return render(request,'manage_profile.html',{'user':user,'msg':msg})

def search_artist(request):
    artist=register_artist.objects.all()
    return render(request,'search_artist.html',{'artist':artist})

def book_artist(request):
    msg=""
    user_id = request.session.get('user_id')
    if request.method=='POST':
        form=artist_booking_form(request.POST)

        if form.is_valid():
            booking=form.save(commit=False)
            booking.user = user_register.objects.get(id=user_id)  # associate user
            booking.save()
            msg="booked successfuly"
            return redirect('manage_booking')
        else:
            print(form.errors)
            msg="Booking Failed"
    else:
        form = artist_booking_form()
    return render(request,'book_artist.html',{'form': form,'msg':msg})

def cancel_booking(request):
    return render(request,'cancel_booking.html')

def feedback(request):
    user_id = request.session.get('user_id')
    
    if request.method == 'POST':
        form = feedback_form(request.POST)
        
        if form.is_valid():
            fb = form.save(commit=False)
            fb.user = user_register.objects.get(id=user_id)
            fb.save()
            print("feedback sent")
            return redirect('feedback')
        else:
            print(form.errors)
    
    return render(request, 'feedback.html', {'form': feedback_form()})  

def manage_booking(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = user_register.objects.get(id=user_id)

    bookings=book_artist_cls.objects.filter(user=user)

    return render(request,'manage_booking.html',{'bookings':bookings })

def userlogout(request):
    logout(request)
    return redirect('/')

def cancel_booking(request,booking_id):
    booking = book_artist_cls.objects.get(id=booking_id)
    booking.delete()
    return redirect('manage_booking')
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from customer.models import *

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
    msg =""
    user_id=request.session.get('user_id')
    if not user_id:               # session empty છે → login page redirect
        return redirect('login')
    try:
        user=register_artist.objects.get(id=user_id)
    except register_artist.DoesNotExist:
        return redirect('login') 
    if request.method=='POST':
        update_profile=artist_form(request.POST,instance=user)  #instance old data mate che 
        if update_profile.is_valid():
            update_profile.save()
            msg="Profile Updated Successfully!"
        else:
            msg=update_profile.errors
    return render(request,'artist_manage_profile.html',{'user':user,'msg':msg})

def artist_upload_media(request):
    msg=""
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('artist_login')
    artist = register_artist.objects.get(id=user_id)
    if request.method=='POST':
        form = artist_file_form(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=artist
            obj.save()
            msg = "file uploded successfully"
        else:
            msg = form.errors
    else:
        form = artist_file_form()
    return render(request,'artist_upload_media.html',{'msg':msg,'form':form})

def artist_feedback(request):
    msg=""
    user_id = request.session.get('user_id')

    if request.method=='POST':
        form=artist_feedback_form(request.POST)

        if form.is_valid():
            fb=form.save(commit=False)
            fb.user=register_artist.objects.get(id=user_id)
            fb.save()
            msg="feedback sent !"
            return redirect('artist_feedback')
        else:
            msg=form.errors
    return render(request,'artist_feedback.html',{'form': artist_feedback_form()})

def artist_view_booking(request):
    booking = book_artist_cls.objects.all()
    return render(request, 'artist_view_booking.html', {'booking': booking})

def delete_booking(request,id):
    booking=get_object_or_404(book_artist_cls,id=id)
    booking.delete()
    return redirect('artist_view_booking')

def booking_approve(request, id):
    b = get_object_or_404(book_artist_cls, id=id)
    b.status = "Approved"
    b.save()
    return redirect('artist_view_booking')


def booking_reject(request, id):
    b = get_object_or_404(book_artist_cls, id=id)
    b.status = "Rejected"
    b.save()
    return redirect('artist_view_booking')

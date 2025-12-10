from django.shortcuts import render,redirect
from django.contrib.auth import logout
from customer.models import *
from artist.models import *
from django.shortcuts import get_object_or_404
from datetime import datetime

# Create your views here.

def admin_login(request):
    msg=""
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if username=="admin" and password=="123":
            request.session['admin_login'] = True
            print("login admin")
            return redirect("admin_dashboard")
        else:
            msg="Wrong username or password"
    return render(request,'admin_login.html',{'msg':msg})

def manage_users(request):
    users = user_register.objects.all()
    return render(request,'manage_users.html',{'users':users})

def view_bookings(request):
    user_id=request.session.get('user_id')
    customers = user_register.objects.filter(id=user_id)
    artist = register_artist.objects.filter(id=user_id)
    b=book_artist_cls.objects.all()
    return render(request,'view_bookings.html',{'b':b,'customers':customers,'artist':artist})

def view_reviews(request):
    return render(request,'view_reviews.html')

def approve_artist(request):
    artist_bookings = book_artist_cls.objects.all()
    artist = register_artist.objects.all()
    return render(request,'approve_artist.html',{'artist':artist})

def view_feedbacks(request):
    feedback=feedback_cls.objects.all()
    return render(request,'view_feedbacks.html',{'feedback':feedback})

def admin_dashboard(request):
    u=user_register.objects.all()
    a=register_artist.objects.all()
    b=book_artist_cls.objects.all()

    user_id = request.session.get('user_id')
    customers = user_register.objects.filter(id=user_id)
    artist = register_artist.objects.filter(id=user_id)

    total_u=len(u)
    total_a=len(a)
    total_b=len(b)

    return render (request,'admin_dashboard.html',{'total_u':total_u,'total_a':total_a,'total_b':total_b,'b':b})


def admin_logout(request):
    # જો સેશનમાં admin_id હોય તો તેને ડિલીટ કરો
    try:
        del request.session['admin_id']
    except KeyError:
        pass
    
    # Django નું સ્ટાન્ડર્ડ logout પણ કોલ કરો (સલામતી માટે)
    logout(request)
    
    return redirect('admin_login')

def customer_approve(request,id):
    nid=get_object_or_404(register_artist,id=id)
    nid.status="Approve"
    nid.updated_at=datetime.now()
    nid.save()
    
    #Email Sending Code
    customer = register_artist.objects.all()
    return render(request,'approve_artist.html',{'customer' :customer})
    
def customer_reject(request,id):
    nid=get_object_or_404(register_artist,id=id)
    nid.status="Reject"
    nid.updated_at=datetime.now()
    nid.save()
    
    #Email Sending Code
    customer = register_artist.objects.all()
    return render(request,'approve_artist.html',{'customer':customer})

def delete_user(request,id):
    nid=get_object_or_404(user_register,id=id)
    nid.delete()
    return redirect('manage_users')

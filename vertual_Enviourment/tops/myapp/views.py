from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
import random
from tops import settings

# Create your views here.

def index(request):
    user = request.session.get('email')
    return render(request, 'index.html', {'user': user})

def login(request):
    ms =""
    if request.method == 'POST':
        ue = request.POST['email']
        up = request.POST['password']

        user = userdata.objects.filter(email=ue,password=up)
        if user:
            ms = "Login Successful"
            request.session['email'] = ue
            return redirect('/')
        else:
            ms = "Login Failed"
    return render(request,'login.html',{'ms': ms})

def signup(request):
    msg=""
    if request.method == 'POST':
        form = signupform(request.POST)
        email = request.POST['email']
        if userdata.objects.filter(email=email).exists():
            msg = "Email already exists please login"
        else:
         if form.is_valid():
            form.save()

            # otp email sending logic can be added here
            global otp
            otp = random.randint(1000,9999)
            sub = "your otp verification"
            mail_msg = f"dear user \n\n tnx for registration with us \n your email verification OTP is{otp} your otp is valid for 10 minutes \n\n regards \n team"
            from_id=settings.EMAIL_HOST_USER
            to_id = request.POST['email']

            send_mail(subject=sub, message=mail_msg, from_email=from_id, recipient_list=[to_id], fail_silently=False)
            return redirect('otp')
    else:
        msg = "Form is invalid"
    return render(request,'signup.html',{'msg': msg})

def userlogout(request):
    logout(request)
    return redirect('/')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def otp(request):
    global otp
    msg=""
    print(otp)
    if request.method == 'POST':
        if request.POST["otp"] == str(otp):
            msg = "OTP verified successfully"
            return redirect('login')
        else:
            msg = "OTP verification failed"
    return render(request, 'otp.html', {'msg': msg})
from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
import random
from tops import settings
from adminapp.models import * 

# Create your views here.

def index(request):
    user = request.session.get('email')
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    total_price = 0
    for key, item in cart.items():
        if isinstance(item, dict): 
            total_price += float(item['price']) * int(item['qty'])

    context = {
        'user':user,
        'products': products,
        'cart': cart,
        'total': total_price
    }
    return render(request, 'index.html', context)

def login(request):
    ms=""
    if request.method == 'POST':
        ue = request.POST['email']
        up = request.POST['password']

        user = userdata.objects.filter(email=ue,password=up).first()
        if user:
            ms = "Login Successful"
            request.session['email'] = ue
            request.session['fullname'] = user.fullname
            return redirect('/')
        else:
            ms = "Login Failed"
    return render(request,'login.html',{'ms': ms})

def signup(request):
    msg = ""

    if request.method == 'POST':
        form = signupform(request.POST)
        email = request.POST.get('email')
        mobile = request.POST.get("mobil")

        # ---------- 1. Mobile number validation ----------
        if len(mobile) != 10 or not mobile.isdigit():
            return render(request, "signup.html", {"msg": "Mobile number must be exactly 10 digits"})

        # ---------- 2. Email already exists ----------
        if userdata.objects.filter(email=email).exists():
            return render(request, "signup.html", {"msg": "Email already exists please login"})

        # ---------- 3. Form validation ----------
        if form.is_valid():
            form.save()

            # ---------- 4. OTP Send ----------
            global otp
            otp = random.randint(1000, 9999)
            sub = "Your OTP Verification"

            mail_msg = (
                f"Dear user,\n\n"
                f"Thanks for registration with us.\n"
                f"Your verification OTP is {otp}.\n"
                f"OTP valid for 10 minutes.\n\n"
                f"Regards,\nTeam"
            )

            from_id = settings.EMAIL_HOST_USER
            to_id = email

            send_mail(sub, mail_msg, from_id, [to_id], fail_silently=False)

            return redirect('otp')
        else:
            msg = "Form is invalid"

    # GET request = form load
    return render(request, 'signup.html', {'msg': msg})

def userlogout(request):
    if 'email' in request.session:
        del request.session['email']
    if 'fullname' in request.session:
        del request.session['fullname']
    return redirect('/')


def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        newcon=contactform(request.POST)
        if newcon.is_valid():
            newcon.save()
        else:
            print(newcon.errors)
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

def notes(request):
    user = request.session.get("email")
    if not user:
        return redirect('login')
    cuser = userdata.objects.get(email=user)
    if request.method == 'POST':
        form=notesform(request.POST,request.FILES)
        if form.is_valid():
            x=form.save(commit=False)
            x.status="Pending"
            x.user=cuser
            x.save()
            print("done")
        else:
            print("nooooooo")
    return render(request,'notes.html',{'user':user})


def cart(request):
    # Session mathi data lavo
    cart = request.session.get('cart', {})
    
    grand_total = 0
    
    # Loop feravi ne calculation karo
    for key, item in cart.items():
        if isinstance(item, dict):
            # String mathi number ma convert karo
            qty = int(item['qty'])
            price = float(item['price'])
            
            # Ahiya j gunakar (multiply) kari do
            subtotal = qty * price
            
            # Aa subtotal ne item dictionary ma add karo
            item['my_total'] = subtotal
            
            # Grand total ma add karo
            grand_total += subtotal

    # HTML ma data mokalo
    return render(request, 'cart.html', {'cart': cart, 'total': grand_total})

def profile(request):
    email=request.session.get('email')

    if not email:
        return redirect('login')
    
    user_obj = userdata.objects.get(email=email)
    if request.method == 'POST':
        # Check karo ke photo aayo che ke nai
        if 'profile_pic' in request.FILES:
            user_obj.profile_pic = request.FILES['profile_pic']
            user_obj.save()
            print("Profile Picture Updated!") # Terminal ma confirm thase
            return redirect('profile')

    return render(request,'profile.html',{'user':user_obj})

def add_to_cart(request, id):
    # Product database mathi lavo
    user = request.session.get("email")
    if not user:
        return redirect('login')
    product = get_object_or_404(Product, id=id)
    
    # Session cart melvo
    cart = request.session.get('cart', {})
    
    # ID ne string ma fervo (Session keys string hovi joie)
    str_id = str(id)

    if str_id in cart:
        # Jo product already cart ma hoi to qty vadharo
        cart[str_id]['qty'] += 1
    else:
        # Navi product add karo (Dictionary banavi ne)
        cart[str_id] = {
            'qty': 1,
            'price': str(product.price), # Price store kari
            'name': product.name,
            'image': product.image.url if product.image else ''
        }
    
    request.session['cart'] = cart
    return redirect('/')

def update_cart(request, id):
    cart = request.session.get('cart', {})
    str_id = str(id)

    if str_id in cart:
        # Fakt Qty vadharo
        cart[str_id]['qty'] += 1
        
        # NOTE: Ahiya 'my_total' ganvani jarur nathi. 
        # Karan ke 'cart' view automatic ganatri kare che.

    request.session['cart'] = cart
    return redirect('cart')  # Fakt url name, html file nai

def remove_cart(request, id):
    cart = request.session.get('cart', {})
    str_id = str(id)

    if str_id in cart:
        cart.pop(str_id) # Item delete karo

    request.session['cart'] = cart
    return redirect('cart')

def increase_cart(request, id):
    cart = request.session.get('cart', {})
    str_id = str(id)
    if str_id in cart:
        cart[str_id]['qty'] += 1
        request.session['cart'] = cart
    return redirect('cart')

def decrease_cart(request, id):
    cart = request.session.get('cart', {})
    str_id = str(id)
    if str_id in cart:
        cart[str_id]['qty'] -= 1
        if cart[str_id]['qty'] <= 0:
            cart.pop(str_id)
        request.session['cart'] = cart
    return redirect('cart')

def update_profile(request,id):
    user=userdata.objects.get(id=id)

    if request.method=='POST':
        update_user=signupform(request.POST,instance=user)
        if update_user.is_valid():
            update_user.save()
            return redirect('/')
        else:
            print(update_user.errors)
    return render(request,'update_profile.html',{'user':user})

def proced(request):
    return render(request,'proced.html')
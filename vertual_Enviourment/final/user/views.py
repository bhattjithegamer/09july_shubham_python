from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from adminapp.models import *
from django.contrib import messages
from .models import *
from .models import Product, Cart, wishlist as WishlistModel 
import random 
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    return render(request, 'contact.html')

def shop(request):
    products = Product.objects.all()
    user_id = request.session.get('user_id')
    wishlist_ids = []

    if user_id:
        wishlist_ids = list(WishlistModel.objects.filter(user_id=user_id).values_list('product_id', flat=True))

    return render(request, 'shop.html', {'products': products, 'wishlist_ids': wishlist_ids})

def product(request):
    products = Product.objects.all()
    return render(request, 'product.html',{'products': products})

def product_details(request, id):
    product = get_object_or_404(Product, id=id) 
    return render(request, 'product.html', {'products': [product]})

def order_detail(request, id):
    order_obj  = get_object_or_404(payment_cls, id=id)
    items = orderitem_cls.objects.filter(order=order_obj) 

    return render(request, 'order_detail.html', {'order': order_obj, 'items': items})

def cart(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    items = Cart.objects.filter(user_id=user_id)

    total = 0
    for item in items:
        item.total_price = item.product.price * item.quantity
        total += item.total_price

    return render(request, 'cart.html', {
        'cart': items,
        'total': total
    })



def add_to_cart(request, id):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('login')

    product = get_object_or_404(Product, id=id)

    cart_item, created = Cart.objects.get_or_create(
        user_id=user_id,   # ✅ CORRECT
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

def checkout(request):
    user_id = request.session.get('user_id')
    if not user_id: 
        return redirect('login')

    items = Cart.objects.filter(user_id=user_id)
    total = sum(i.product.price * i.quantity for i in items)

    if request.method == 'POST':
        form = payment_form(request.POST)
        if form.is_valid():
            pay = form.save(commit=False)
            pay.user_id = user_id
            pay.total_amount = total
            method = request.POST.get('payment_method')

            pay.cash_on_delivery = (method == 'cod')
            
            if method != 'card': pay.debit_card_number = pay.mm_yy = pay.cvv = None
            if method != 'upi': pay.upi_id = None
            
            pay.save() 

            for item in items:
                orderitem_cls.objects.create(
                    order=pay,                
                    product=item.product,     
                    quantity=item.quantity,   
                    price=item.product.price  
                )

            items.delete() 
            return render(request, 'checkout.html', {'success': True})

    return render(request, 'checkout.html', {'total': total})

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = user_register.objects.filter(email=email,password=password).first()
        if user:
            request.session['user_id'] = user.id
            return redirect('index')
        else:
            msg = "Invalid Credentials"
            return render(request, 'login.html', {'msg': msg})
    return render(request, 'login.html')

def register(request):
    msg = ""
    if request.method == 'POST':
        email = request.POST.get('email')

        if user_register.objects.filter(email=email).exists():
            msg = "Email already exists, please login"
            return render(request, 'register.html', {'msg': msg})

        form = user_register_form(request.POST)
        if form.is_valid():
            user = form.save()

            otp = random.randint(1111, 9999)

            sub = "Your OTP for Verification"
            mail_msg = f"Dear User,\n\nYour OTP is {otp}.\n\nRegards,\nNotesApp Team Bhattji"
            
            try:
                send_mail(sub, mail_msg, settings.EMAIL_HOST_USER, [email])
                
                request.session['otp'] = otp
                request.session['email'] = email 
                
                return redirect('otp_ver') # Tamaru URL name check kari lejo
            except Exception as e:
                msg = "Network Error. Please try again."
        else:
            msg = "Invalid Form Data"

    return render(request, 'register.html', {'msg': msg})

def otp_ver(request):
    msg = ""
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        generated_otp = request.session.get('otp') # Session mathi OTP lavo

        if str(entered_otp) == str(generated_otp):
            # Verification Successful
            del request.session['otp'] # Session clear karo
            return redirect('login')
        else:
            msg = "Invalid OTP. Please try again."
    
    return render(request, 'otp_ver.html', {'msg': msg})

def blog(request): 
    return render(request, 'blog.html')

def blog_item(request): 
    return render(request, 'blog-item.html')

def careers(request): 
    return render(request, 'careers.html')

def faq(request): 
    return render(request, 'faq.html')

def gallery(request): 
    products = Product.objects.all()
    return render(request, 'gallery.html', {'products': products})

def order_success(request): 
    return render(request, 'order-success.html')

def orders(request): 
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    orders = payment_cls.objects.filter(user_id=user_id).order_by('-created_at')
     
    return render(request, 'orders.html', {'orders': orders})

def privacy_policy(request): 
    return render(request, 'privacy-policy.html')

def product_3d_viewer(request): 
    return render(request, 'product-3d-viewer.html')

def profile(request): 
    like = wishlist.objects.filter(user_id=user_id)
    orders = payment_cls.objects.filter(user_id=user_id)

    total_like = len(like)
    total_orders = len(orders)

    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    user = user_register.objects.filter(id=user_id).first()
    return render(request, 'profile.html', {'user': user, 'total_orders': total_orders, 'total_like': total_like})

def search_results(request): 
    return render(request, 'search-results.html')

def terms(request): 
    return render(request, 'terms.html')

# આ ફંક્શનનું નામ 'wishlist' ન હોવું જોઈએ, 'wishlist_page' રાખો
def wishlist_page(request):
    user_id = request.session.get('user_id')
    if not user_id: 
        return redirect('login')
    
    w_items = WishlistModel.objects.filter(user_id=user_id) 
    return render(request, 'wishlist.html', {'w_items': w_items})

def toggle_wishlist(request, pid):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    item = WishlistModel.objects.filter(user_id=user_id, product_id=pid)
    if item.exists():
        item.delete()
    else:
        WishlistModel.objects.create(user_id=user_id, product_id=pid)
    
    return redirect(request.META.get('HTTP_REFERER', '/'))
def page_1(request): 
    return render(request, 'page-1.html')

def page_2(request): 
    return render(request, 'page-2.html')

def page_3(request): 
    return render(request, 'page-3.html')

def page_4(request): 
    return render(request, 'page-4.html')

def page_5(request): 
    return render(request, 'page-5.html')

def user_logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('login')

def delete_cart(request,id):
    cart_item = get_object_or_404(Cart, id=id)
    cart_item.delete()
    return redirect('cart')
    
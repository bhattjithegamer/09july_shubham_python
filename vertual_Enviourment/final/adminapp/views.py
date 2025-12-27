from django.shortcuts import render,get_list_or_404,redirect,get_object_or_404
from adminapp.models import *
from user.models import * 
from django.contrib.auth import logout

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == "admin" and password == "123":
            request.session['admin_logged_in'] = True
            return redirect('dashboard')
        else:
            return render(request, "admin_login.html", {"error": "Invalid credentials"})
    return render(request, "admin_login.html")

def dashboard(request):
    user = user_register.objects.all()
    products = Product.objects.all()
    sale = payment_cls.objects.all()
    message = contact_cls.objects.all()

    total_user = len(user)
    total_product = len(products)
    total_sale = len(sale)
    total_message = len(message)
    order = payment_cls.objects.all().order_by('-id')
    return render(request, "dashboard.html", {"total_user": total_user, "total_product": total_product, "total_sale": total_sale, "order": order,"total_message":total_message})

def products(request):
    products = Product.objects.all()
    return render(request, "products.html",{'products':products})

def add_product(request):
    if request.method == "POST":
        data = request.POST.dict()
        data.pop('csrfmiddlewaretoken')  # ← error fix

        Product.objects.create(**data,image=request.FILES.get('image'))
        return redirect('products')

    return render(request, 'add_product.html')


def edit_product(request,id):
    product = Product.objects.get(id=id)
    return render(request, "edit_product.html",{'product':product})

def admin_orders(request):
    orders = payment_cls.objects.all().order_by('-id')
    return render(request, "admin_orders.html", {"orders": orders})

def order_details(request, id):
    return render(request, "order_details.html", {"order_id": id})

def users(request):
    users = user_register.objects.all()
    return render(request, "users.html", {"users": users})

def settings(request):
    return render(request, "settings.html")

def update_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        fields = ['title', 'price', 'stock', 'category', 'description', 
                  'processor', 'ram', 'storage', 'graphics', 'display']
        
        for field in fields:
            setattr(product, field, request.POST.get(field))

        if request.FILES.get('image'):
            product.image = request.FILES['image']

        product.save()
        return redirect('products')

    return render(request, 'edit_product.html', {'product': product})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('products')

def block_user(request, id):
    user = get_object_or_404(user_register, id=id)
    user.delete()
    return redirect('users')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

def admin_contact_list(request):
    contacts = contact_cls.objects.all().order_by('-id')
    return render(request, "admin_contact_list.html", {"contacts": contacts})

def delete_contact(request, id):
    contact = get_object_or_404(contact_cls, id=id)
    contact.delete()
    return redirect('admin_contact_list')

def admin_settings(request):
    if request.method == 'POST':
        color = request.POST.get('bg_color') # HTML માંથી કલર લાવો
        
        request.session['admin_bg_color'] = color 
        
        return redirect('admin_settings') # પેજ રિફ્રેશ કરો

    return render(request, 'admin_settings.html')
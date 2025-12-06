from django.shortcuts import render,redirect, get_object_or_404
from myapp .models import *
from django.contrib.auth import logout
from myapp .forms import *
from datetime import datetime
from tops import settings
from django.core.mail import send_mail

# Create your views here.

def admin_login(request):
    if request.method=='POST':
        un=request.POST["username"]
        pas=request.POST["password"]

        if un=="admin" and pas=="admin@123":
            return redirect('admin_dashboard')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid Credentials'})
    return render(request,'admin_login.html')

def admin_dashboard(request):
    u=userdata.objects.all()
    n=mynotes.objects.all()
    totaluser=len(u)
    totalnotes=len(n)
    return render(request,'admin_dashboard.html',{'totaluser':totaluser , 'totalnotes' : totalnotes})

def admin_userdata(request):
    data=userdata.objects.all()
    return render(request,'admin_userdata.html',{'data':data})

def admin_notesdata(request):
    ndata=mynotes.objects.all()
    return render(request, 'admin_notesdata.html', {'ndata': ndata})


def adminlogout(request):
    logout(request)
    return redirect('admin_login')

def admin_product(request):
    # Badho data variable ma lavo
    products = Product.objects.all() 
    
    # Template ma 'products' key thi data mokalo
    return render(request, 'admin_product.html', {'products': products}) 

# Add Product View (Sudharelo Code)
def admin_add_pro(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            image=image
        )
        return redirect('admin_product')
    return render(request, 'admin_add_pro.html')

def deleteproduct(request,id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect('admin_product')

def notes_approve(request, id):
    nid = get_object_or_404(mynotes, id=id)
    nid.status = "approve"
    nid.updated_at = datetime.now()
    nid.save()
   
    sub = "Your Notes Approved"
    email = nid.user.email          # User no email mynotes model ma hoy to

    mail_msg = (
        f"Dear user,\n\n"
        f"Your notes has been approved successfully.\n"
        f"Regards,\nTeam Bhatt ji"
    )

    from_id = settings.EMAIL_HOST_USER
    to_id = email

    send_mail(
        sub,
        mail_msg,   
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )

    return redirect('admin_notesdata')


def notes_reject(request,id):
    nid=get_object_or_404(mynotes,id=id)
    nid.status="reject"
    nid.updated_at=datetime.now()
    nid.save()
    sub = "Your Notes Approved"
    email = nid.user.email          # User no email mynotes model ma hoy to

    mail_msg = (
        f"Dear user,\n\n"
        f"Your notes has been rejected.\n"
        f"Regards,\nTeam Bhatt ji"
    )

    from_id = settings.EMAIL_HOST_USER
    to_id = email

    send_mail(
        sub,
        mail_msg,   
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )

    return redirect('admin_notesdata')
    

from django.shortcuts import render, get_object_or_404,redirect
from user .models import userlogin,post 


# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')

def all_posts(request):
    posts = post.objects.all()
    return render(request,'posts.html',{'posts': posts})

def users_list(request):
    users = userlogin.objects.all()  # ડેટાબેઝમાંથી બધા યુઝર લાવશે
    return render(request,'users.html', {'users': users})

def detail_post(request, id):
    # ડેટાબેઝમાંથી ID મુજબ પોસ્ટ લાવો
    post = get_object_or_404(post, id=id) 
    
    # detail.html માં ડેટા મોકલો
    return render(request, 'detail.html', {'post': post})

def delete_user(request, id):
    # જે યુઝરને ડિલીટ કરવો હોય તેને ID થી શોધો
    user_obj = get_object_or_404(userlogin, id=id) 
    
    # યુઝરને ડિલીટ કરો
    user_obj.delete()
    
    # પાછા લિસ્ટ પેજ પર રીડાયરેક્ટ કરો (અહીં 'manage_users' એ તમારા લિસ્ટ પેજનું URL name હોવું જોઈએ)
    return redirect('manage_users')
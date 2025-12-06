from django.shortcuts import render

# Create your views here.

def admin_login(request):
    return render(request,'admin_login.html')

def manage_users(request):
    return render(request,'manage_users.html')

def view_bookings(request):
    return render(request,'view_bookings.html')

def view_reviews(request):
    return render(request,'view_reviews.html')

def approve_artist(request):
    return render(request,'approve_artist.html')

def view_feedbacks(request):
    return render(request,'view_feedbacks.html')

def admin_dashboard(request):
    return render (request,'admin_dashboard.html')
from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def all_posts(request):
    return render(request, 'posts.html')
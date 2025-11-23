from django.shortcuts import render
import random
counter = 0

# Create your views here.
def login(request):
    return render(request, 'login.html')
def register(request):
    name = 'bhattji'
    num = random.randint(1,10000)
    global counter
    counter += 1
    return render(request,'register.html',{'name':name,'num':num,'counter':counter})
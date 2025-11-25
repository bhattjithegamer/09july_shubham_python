from django.shortcuts import render, redirect
from .models import Student

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')

        Student.objects.create(name=name, age=age, city=city)

        return redirect('list')

    return render(request, 'create.html')

def list(request):
    students = Student.objects.all()  # ORM READ
    return render(request, 'list.html', {'students': students})

def update(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.city = request.POST.get('city')
        student.save()   # ORM UPDATE

        return redirect('list')

    return render(request, 'update.html', {'student': student})

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()   # ORM DELETE
    return redirect('list')

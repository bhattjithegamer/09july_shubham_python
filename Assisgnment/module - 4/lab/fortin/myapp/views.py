from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        student = Student.objects.create(name=name, email=email)
        return JsonResponse({
            'id': student.id,
            'name': student.name,
            'email': student.email
        })

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return JsonResponse({'status': 'deleted'})

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.save()
        return JsonResponse({
            'id': student.id,
            'name': student.name,
            'email': student.email
        })

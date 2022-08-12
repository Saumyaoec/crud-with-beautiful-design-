from django.shortcuts import render, redirect
from .models import StudentData

def mainpage(request):
    student=StudentData.objects.all()
    return render(request,'homepage1.html', {'student':student})

def add_student(request):
    if request.method =="GET":
        return render(request, 'add_student.html')
    else:
        StudentData(
        task=request.POST.get('fname'),
        description=request.POST.get('mobile'),

        ).save()
        return redirect('mainpage')

def update_student(request, id):
    student=StudentData.objects.get(id=id)
    if request.method=='GET':
        return render(request, 'update_student.html', {'student':student})
    else:
        student.task=request.POST.get('fname')
        student.description=request.POST.get('Description')
        student.save()
        return redirect('mainpage')

def delete_student(request, id):
    student=StudentData.objects.get(id=id)
    student.delete()
    return redirect('mainpage')

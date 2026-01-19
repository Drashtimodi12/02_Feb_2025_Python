from django.shortcuts import render,redirect
from myapp.models import *
import os
# Create your views here.
def index(request):
    allStudents  = Student.objects.all()
    return render(request,"index.html",{"students":allStudents})

def register(request):
   
   
    if request.method=='POST':
        data = request.POST
        id = data.get("id")
        username = data.get("uname")
        email = data.get("email")
        phone = data.get("phone")
        age = data.get("age")
        image = request.FILES['file']

        if(id):
            student = Student.objects.get(pk=id)
            student.username=username
            student.email= email
            student.phone=phone
            student.age=age
            os.remove(student.image.path)
            student.image=request.FILES['file']
            student.save()
            return redirect("index")
        else:
            st =  Student.objects.create(username=username,email=email,phone=phone,age=age,image=image)
            if(st):
                #return render(request,'index.html',{"msg":"Registration successful"})
                return redirect("index")

    return render(request,'index.html')

def delete(request):
    stid =  request.GET['stid']
    student = Student.objects.get(pk=stid)
    os.remove(student.image.path)
    student.delete()
    return redirect("index")

def update(request):
    stid =  request.GET['stid']
    student = Student.objects.get(pk=stid)
    allStudents  = Student.objects.all()
    return render(request,"index.html",{"student":student,"students":allStudents})


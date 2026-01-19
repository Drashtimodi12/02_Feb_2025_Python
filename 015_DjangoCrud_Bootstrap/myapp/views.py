from django.shortcuts import render,redirect
from myapp.models import *
import os
# Create your views here.
def index(request):
    allStudents = Student.objects.all()
    return render(request,"index.html",{"students":allStudents})

def register(request):
    if request.method=='POST':
        id = request.POST['id']
        username = request.POST['uname']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']
        image = ""
        if request.FILES : 
            image = request.FILES['img']

        if(id):
            stud = Student.objects.get(pk=id)     
            stud.username=username
            stud.email = email
            stud.phone=phone
            stud.age=age
            if image : 
                os.remove(stud.image.path)
                stud.image=image
            stud.save()
        else :
            Student.objects.create(username=username,email=email,phone=phone,age=age,image=image)
            # return render(request,"index.html",{"msg":"Registration successfully"})
        return redirect("index")

    return redirect("index")


def delete(request):
    sid = request.GET['sid']
    student = Student.objects.get(pk=sid)
    os.remove(student.image.path)
    student.delete()
    return redirect("index")
   

def edit(request):
    sid = request.GET['sid']
    student = Student.objects.get(pk=sid)
    allStudents = Student.objects.all()
    return render(request,"index.html",{"students":allStudents,"student":student})
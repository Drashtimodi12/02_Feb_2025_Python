from django.shortcuts import render,HttpResponse
from crudapp.models import Student
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,"home.html")

def adddata(request):
    
    if request.method=='POST':
        data = request.POST
        uname = data.get("uname")
        email = data.get("email")
        age = data.get("age")

        Student.objects.create(username=uname,email=email,age=age)
        return HttpResponse("Registration successfully !!!")
    
def loaddata(request):
    alldata = Student.objects.all()
    return JsonResponse({"data":list(alldata.values())})

def deletedata(request):
    sid = request.GET['sid']
    students = Student.objects.get(pk=sid)
    students.delete()
    return HttpResponse("Student deleted !!!")

def databyid(request):
    sid = request.GET['sid']
    student = Student.objects.filter(id=sid)
    return JsonResponse({"data":list(student.values())})

def updatedata(request):
    if request.method=='POST':
        data = request.POST
        id = data.get("id")

        student = Student.objects.get(pk=id)
        student.username = data.get("uname")
        student.email = data.get("email")
        student.age = data.get("age")

        student.save()
        return HttpResponse("Update successfully !!!!")
    

def searchdata(request):

    keyword = request.GET['value']
    filterdData = Student.objects.filter(username__startswith=keyword)
    return JsonResponse({"data":list(filterdData.values())})
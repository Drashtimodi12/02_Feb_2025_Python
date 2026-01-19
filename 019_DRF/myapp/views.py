from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from myapp.models import *
from myapp.serializer import *

# Create your views here.
@api_view(['GET'])
def index(request):
    allStudents = Student.objects.all()
    ser = StudentSerializer(allStudents,many=True)
    return Response({"students":ser.data})

@api_view(['POST'])
def add(request):
    try :
        ser =  StudentSerializer(data= request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors,"message":"something went wrong"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"Data inserted successfully"})
    except Exception as e:
        print(e)
        return Response({"error":e,"message":"something went wrong"})


@api_view(['PUT'])
def update(request,id):
    try:
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student,request.data,partial=True)
        if not ser.is_valid():
            return Response({"errors":ser.errors,"message":"something went wrong"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"Data updated successfully"})
    except Exception as e:
        return Response({"error":e,"message":"something went wrong"})

@api_view(["DELETE"])
def delete(request,id):

    try:
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({"success":True})
    except Exception as e:
         return Response({"error":e,"message":"something went wrong"})
    

@api_view(["GET"])
def getemp(request):
    try:
        allemp = Emp.objects.all()
        ser = EmpSerializer(allemp,many=True)
        return Response({"data":ser.data})
    except Exception as e:
        return Response({"message":"Something went wrong"})

@api_view(["POST"])
def addemp(request):
    try : 
        ser = EmpSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"Errors":ser.errors,"message":"Something went wrong"})
        ser.save()
        return Response({"Inserted data":ser.data})
    except Exception as e:
         return Response({"message":"Something went wrong"})

@api_view(["PUT"])
def updateemp(request,id):
    try : 
        empdata = Emp.objects.get(pk=id)
        ser = EmpSerializer(empdata,request.data)
        if not ser.is_valid():
            return Response({"Errors":ser.errors,"message":"Something went wrong"})
        ser.save()
        return Response({"updated data":ser.data})
    except Exception as e:
         return Response({"message":"Something went wrong"})

@api_view(["DELETE"])
def deleteemp(request,id):
    try : 
        empdata = Emp.objects.get(pk=id)
        empdata.delete()
        return Response({"success":True})
    except Exception as e:
         return Response({"message":"Something went wrong"})
    


class ProductAPI(APIView):
    def get(self,request):
        try:
            allproducts = Product.objects.all()
            ser = ProductSerializer(allproducts,many=True)
            return Response({"data":ser.data})
        except Exception as e:
            return Response({"message":"Something went wrong"})

    def post(self,request):
        try:
            ser = ProductSerializer(data=request.data)
            if not ser.is_valid():
                return Response({"Errors":ser.errors,"message":"Something went wrong"})
            ser.save()
            return Response({"Inserted data":ser.data})
        except Exception as e:
            return Response({"message":"Something went wrong"})
        
    def put(self,request):
        try:
            product = Product.objects.get(pk=request.data.get('id'))
            if not product:
                return Response({"message":"Product not found"})    
            ser = ProductSerializer(product,request.data)
            if not ser.is_valid():
                return Response({"Errors":ser.errors,"message":"Something went wrong"})
            ser.save()
            return Response({"Updated data":ser.data})
        except Exception as e:
            return Response({"message":"Something went wrong"})
        
    def delete(self,request):
        try:
            product = Product.objects.get(pk=request.data.get('id'))
            if not product:
                return Response({"message":"Product not found"})
            product.delete()
            return Response({"success":True})
        except Exception as e:
            return Response({"message":"Something went wrong"})
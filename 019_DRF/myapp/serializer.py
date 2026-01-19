from rest_framework import serializers
from myapp.models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Student
        fields = '__all__'
        #fields= ['id',"username"]
        # exclude=['username']

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
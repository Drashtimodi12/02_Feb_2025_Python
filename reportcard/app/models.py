from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=20)

class StudentId(models.Model):
    stid = models.CharField(max_length=10)

class Student(models.Model):
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    stid = models.ForeignKey(StudentId,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email  =models.CharField(max_length=50)
    age = models.IntegerField()

class Subject(models.Model):
    name = models.CharField(max_length=20)

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)

from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()


class Emp(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    salary = models.FloatField()
    dept = models.CharField(max_length=20)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    stock = models.IntegerField()

   
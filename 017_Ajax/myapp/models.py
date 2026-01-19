from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)

class Country(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=10)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=10)
    state = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
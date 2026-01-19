from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)

class Publication(models.Model):
    name = models.CharField(max_length=20)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    qty = models.IntegerField()



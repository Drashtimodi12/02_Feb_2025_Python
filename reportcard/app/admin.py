from django.contrib import admin
from app.models import *
# Register your models here.

class DepartmentData(admin.ModelAdmin):
    list_display = ["name"]

class SubjectData(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Department,DepartmentData)
admin.site.register(StudentId)
admin.site.register(Student)
admin.site.register(Subject,SubjectData)
admin.site.register(Marks)

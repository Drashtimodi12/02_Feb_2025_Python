from django.urls import path
from myapp.views import *

urlpatterns = [
    path("getstudents",index,name="index"),
    path("addstudent",add,name="add"),
    path("updatestudent/<int:id>",update,name="update"),
    path("deletestudent/<int:id>",delete,name="delete"),


    path("employess",getemp,name="employees"),
    path("employess/",addemp,name="employees/"),
    path("employess/<int:id>",updateemp,name="employees-update/"),
    path("employess/<int:id>/",deleteemp,name="employees-delete/"),

    path("products",ProductAPI.as_view())


]
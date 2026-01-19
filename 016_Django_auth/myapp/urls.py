from django.urls import path
from myapp.views import *
urlpatterns = [
    path("",index,name="index"),
    path("reg",reg,name="reg"),
    path("adduser",adduser,name="adduser"),
    path("loginuser",loginuser,name="loginuser"),
    path("home",home,name="home"),
    path("userlogout",userlogout,name="userlogout")

]


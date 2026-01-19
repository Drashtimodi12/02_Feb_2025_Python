from django.urls import path
from myapp.views import *
from crudapp import views
urlpatterns = [
    
    path("",index,name="index"),
    path("search",search,name="search"),
    path("countries",countries,name="countries"),
    path("states",states,name="states"),
    path("cities",cities,name="cities"),
    path("crud",views.index,name="crud")
]

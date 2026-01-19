from django.urls import path
from app.views import *

urlpatterns = [
    path("",index,name="index"),
    path("marksheet",marksheet,name="marksheet"),
    path("sendmail",sendmail,name="sendmail"),
]
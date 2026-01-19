from django.urls import path
from myapp.views import *

urlpatterns = [
   path('', index, name='index'),
   path('payment', payment, name='payment'),
   path('message', message, name='message'),
   path('sendmail', send_mail_page, name='send_mail_page'),

]



from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("", home, name="home"),
    # create url for accounts, cart,checkout,details,login-register,shop
    path("accounts",accounts,name="accounts"),
    path("cart",cart,name="cart"),
    path("checkout",checkout,name="checkout"),
    path("details",details,name="details"),
    path("login-register",login_register,name="login-register"),
    path("shop",shop,name="shop"),

    path("register-user", register_user, name="register-user"),
    path("login-user", login_user, name="login-user"),
    path("logout-user", logout_user, name="logout-user"),

    path("categories", categories, name="categories"),
    path("products", products, name="products"),

    path("addtocart",addtocart,name="addtocart"),
    path("deletecart",deletecart,name="deletecart"),
    path("changeqty",changeqty,name="changeqty"),

    path('payment', payment, name='payment'),

    path('order', order, name='order'),
   

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
    




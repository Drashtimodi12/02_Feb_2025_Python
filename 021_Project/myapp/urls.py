
from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    #user registration api
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),

    path('categories/', CategoryAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name='category-detail'),

    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product-detail'),

    path('products/category/<int:category_id>/', ProductByCategoryAPIView.as_view(), name='product-by-category'),
    path('products/search/', ProductSearchAPIView.as_view(), name='product-search'),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Cart-related URLs
    
    path('cart/', CartAPIView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', CartAPIView.as_view(), name='cart-detail'),

    #change qty in cart
    path('cart/change-qty/<int:pk>/', ChangeQtyAPIView.as_view(), name='change-qty'),
   

    path("payment",payment,name="payment"),

    path('orders/', OrderAPIView.as_view(), name='order-list'),

   
   
    # path('orders/<int:pk>/', OrderAPIView.as_view(), name='order-detail'),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
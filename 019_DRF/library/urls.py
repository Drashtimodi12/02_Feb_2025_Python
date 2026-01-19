from django.urls import path,include
from library.views import *
# from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    
    path("authors",AuthorAPI.as_view()),
    path("authors/<int:id>",AuthorAPIById.as_view()),

    path("publications",PublicationAPI.as_view()),
    path("publications/<int:id>",PublicationAPIById.as_view()),

    path("books",bookList,name="bookList"),

    path("books/author/<int:aid>/publication/<int:pid>",bookCreate, name="bookCreate"),
    path("books/author/<int:aid>/publication/<int:pid>/<int:id>",bookUpdate, name="bookUpdate"),

    path("books/<int:id>",BookAPIById.as_view()),

    path("books/author/<int:aid>",bookByAuthor, name="bookListByAuthor"),
    path("books/publication/<int:pid>",bookByPublication , name="bookListByPublication"),

    #  path('api-token-auth/', views.obtain_auth_token)

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

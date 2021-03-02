from django.urls import path, include
from .views import register,loginn,logoutUser,profilereg


urlpatterns = [
    path('register/',register,name="register"),
    path('profilereg/',profilereg,name="profilereg"),
    path('login/',loginn,name="login"),
    path('logout/',logoutUser,name="logout"),
] 
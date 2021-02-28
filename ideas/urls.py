
from django.contrib import admin
from django.urls import path, include
from .views import home,register, loginn,logoutUser,sendMail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name="home"),
    path('register/',register,name="register"),
    path('login/',loginn,name="login"),
    path('logout/',logoutUser,name="logout"),
    path('ideas/',include(('Content.urls','ideas')),name='ideas'),
    path('admin/', admin.site.urls),
    path('sendmail/',sendMail,name='sendEmail')
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

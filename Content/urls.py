from django.urls import path
from .views import home,addI,IdeasUpdateView,DetailView

urlpatterns = [
    path('',home,name="home"),
    path('add/',addI,name="addI"),
    path('detail/<int:pk>/',DetailView.as_view(),name="detail"),
    
    path('update/<int:pk>/',IdeasUpdateView.as_view(), name="updatess")
]
from django.urls import path
from .views import home,addI,IdeasUpdateView,DetailView,listIdea,rateIdea

urlpatterns = [
    path('',home,name="home"),
    path('add/',addI,name="addI"),
    path('detail/<int:id>/',DetailView.as_view(),name="idetail"),
    path('category/<int:id>',listIdea,name="ilist"),
    path('update/<int:pk>/',IdeasUpdateView.as_view(), name="updatess"),
    path('rateIdea/<int:id>/',rateIdea, name="rateIdea")

]
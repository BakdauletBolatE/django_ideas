from django.shortcuts import render, redirect

from Content.models import Ideas,ICategory


def home(request):
    lastideas = Ideas.objects.all()[:3] 
    categories = ICategory.objects.all()[:4]

    data = {
        'categories':categories,
        'lastideas':lastideas
    }
        
    return render(request,'home/home.html',data)






           




from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,ContactForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail  
from Content.models import Ideas


def home(request):
    ideas = Ideas.objects.order_by('-rating')[:5] 
    form = ContactForm()
        
    return render(request,'home/home.html',{'posts':ideas,'form':form})

def sendMail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'b.fead@mail.ru',[form.cleaned_data['email']],fail_silently=False)
            if mail:
                messages.success(request,'Сіздің өтініміз жіберілді')
                return redirect('home')
            else:
                messages.error(request,'Жіберілмеді')
                return redirect('home')

           



def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,f"Сіз {user} сәтті тіркелдіңіз")

            return redirect('login')

    context = {
        'form': form,
    }
    
        
    return render(request,'accounts/register.html',context)


def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            messages.success(request,f"Сіз {user} сәтті жүйеге кірдіңіз")
            return redirect('home')
    
    return render(request,'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
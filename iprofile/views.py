from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm,CreateUserForm
# Create your views here.

def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            #authenticate user then login
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,f"Сіз {username} сәтті тіркелдіңіз")

            return redirect('profilereg')

    context = {
        'form': form,
    }
    
        
    return render(request,'accounts/register.html',context)

def profilereg(request):

    if request.method == 'POST':
        profile = ProfileForm(request.POST,request.FILES)
        if profile.is_valid():
            p = profile.save(commit=False)
            
            p.user_id = request.POST.get('user')
            p.save()

            return redirect('home')

    else:

        profile = ProfileForm()
        context = {
            'profile': profile,
        }
        return render(request,'accounts/profilereg.html',context)

def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            messages.success(request,f"Сіз {user} сәтті жүйеге кірдіңіз")
            return redirect('home')
        
        else:
            form = CreateUserForm(request.POST)

            context = {
                'form': form,
            }
            messages.error(request,f"Неверный пароль или логин")
            return render(request,'accounts/login.html',context)
    
    else: 
        form = CreateUserForm()

        context = {
            'form': form,
        }

        return render(request,'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')
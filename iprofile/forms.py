from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['photo','specialization']


class CreateUserForm(UserCreationForm):

    username = forms.CharField(label="Пишите свое имя",
                                widget=forms.TextInput(
                                    attrs={'class':'form-control',
                                    'placeholder':'Пишите свое имя'
                                    }))
    email = forms.CharField(label="Пишите свой Email",
                                widget=forms.TextInput(
                                    attrs={'class':'form-control',
                                    'placeholder':'Пишите свой Email'
                                    })) 
    password1 = forms.CharField(label="Пишите свой пароль",
                                widget=forms.TextInput(
                                    attrs={'class':'form-control',
                                    'placeholder':'Пишите свой пароль'
                                    })) 
    password2 = forms.CharField(label="Повтарите свой пароль",
                                widget=forms.TextInput(
                                    attrs={'class':'form-control',
                                    'placeholder':'Повтарите свой пароль'
                                    })) 

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

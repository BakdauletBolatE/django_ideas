from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    subject = forms.CharField(label="Тақырыбы",
                                widget=forms.TextInput(
                                    attrs={'class':'form-control',
                                    }))
    content = forms.CharField(label="Тақырыбы",
                                widget=forms.TextInput(
                                    attrs={'class':'form-control',
                                    }))
    email = forms.EmailField(label="Тақырыбы",
                                widget=forms.TextInput(
                                    attrs={'class':'form-control',
                                    }))
                                    

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    password1 = forms.CharField(label='Пароль пользователя', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))
    password2 = forms.CharField(label='Пароль пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control '}),
            'email': forms.EmailInput(attrs={'class': 'form-control '}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control '}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control '}),

        }


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'loginforma'}))

    password = forms.CharField(label='Имя пользователя', widget=forms.PasswordInput(
        attrs={'class': 'loginforma'}))

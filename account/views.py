from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.
from account.forms import CustomUserCreationForm

__all__ = [
    'register',
    'sign_in',
    'unlogin',
    'LoginViewVerm',

]


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'register_form': form,
                'message': messages.info(request, 'Вы успешно зарегистрировались!'),
            }
            print(1)
            return render(request, 'portfolio/home.html', context)
        else:
            print(2)
            form = CustomUserCreationForm()
            messages.error(request, 'Ошибка валидации')
            context = {
                'register_form': form,
            }
            return render(request, 'account/register.html', context)
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'register_form': form})


class LoginViewVerm(LoginView):
    """Класс отображения аутентификации пользователя"""
    authentication_form = AuthenticationForm
    template_name = 'account/login.html'


def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('/register/')


def unlogin(request):
    logout(request)
    return redirect('/')



from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.shortcuts import redirect, render
from django.urls import reverse


def login(request):

    context = {
        'title': 'Home - Авторизация',
        # 'form': form
    }
    return render(request, 'login.html', context)


def registration(request):

    context = {
        'title': 'Home - Регистрация',
        # 'form': form
    }
    return render(request, 'registration.html', context)


def profile(request):
    context = {
        'title': 'Home - Кабинет',
        # 'form': form,
        # 'orders': orders,
    }
    return render(request, 'profile.html', context)


# def users_cart(request):
#     return render(request, 'users/users_cart.html')
#

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))

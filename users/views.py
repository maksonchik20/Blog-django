from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserOurRegistation, ProfileImage, UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserOurRegistation(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} успешно зарегистрирован, введите логин и пароль для авторизации')
            return redirect('auth')
    else:
        form = UserOurRegistation()
    return render(request, 'users/registation.html', {'title': 'Регистрация', 'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdateForm(request.POST, instance=request.user)
        if update_user.is_valid() and img_profile.is_valid():
            update_user.save()
            img_profile.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)
    data = {
        'title': "Личный кабинет",
        'img_profile': img_profile,
        'update_user': update_user
        }
    return render(request, 'users/profile.html', data)
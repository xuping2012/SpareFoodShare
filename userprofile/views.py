from django.contrib import auth
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.urls import reverse

from userprofile.models import Profile
from userprofile.userforms import LoginForm, RegistrationForm


def user_login(request):
    # print(request.POST)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("home"))
            else:
                # 登录失败
                print("登录失败")
                return render(request, 'login.html',
                              {'form': form, 'message': '账号或密码错误'})
        else:

            return render(request, 'login.html',
                          {'form': form, 'message': '账号或密码错误'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {"form": form})


def user_register(request):
    print(request.POST)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            nickname = form.cleaned_data['nickname']
            password = form.cleaned_data['password']
            tel_number = form.cleaned_data['tel_number']
            gender = form.cleaned_data['gender']
            type = form.cleaned_data['type']

            # 使用内置User自带create_user方法创建用户，不需要使用save()
            user = Profile.objects.create_user(username=username,
                                               password=password,
                                               email=email,
                                               tel_number=tel_number,
                                               gender=gender,
                                               type=type,
                                               nickname=nickname
                                               )
            print(user)
            # 如果直接使用objects.create()方法后不需要使用save()
            # user_profile = Profile(user)
            # user_profile.save()

            return HttpResponseRedirect(reverse("userprofile:login"))
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

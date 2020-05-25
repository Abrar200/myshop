from django.shortcuts import render, HttpResponseRedirect, Http404, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from django.urls import reverse

def logout_view(request):
    logout(request)
    messages.success(request, f'You have been logged out')
    return HttpResponseRedirect('/')


def account(request):
    return render(request, 'accounts/account.html')


def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, f'Succesfully signed in.')
        return HttpResponseRedirect('/')

    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)
    

def registration_view(request):
    form = RegistrationForm(request.POST or None)

    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.save()
        messages.success(request, f'Your account has been created! You are now able to log in')
        return HttpResponseRedirect(reverse('login'))

    context = {
        "form": form
    }
    return render(request, "accounts/register.html", context)
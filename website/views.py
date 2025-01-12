from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
import os
from django.http import HttpResponseRedirect
from django.urls import reverse


def user_logout(request):
  logout(request)
  messages.success(request, 'You have successfully logged out.')
  return redirect('home')



def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('home')

    else:
        return render(request, 'home.html', {})

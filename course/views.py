from django.shortcuts import render
from django.http import HttpResponse

def homepage1(request):
    return render(request, 'shop/homepage1.html')

def login(request):
    return render(request, 'shop/login.html')

def newuser(request):
    return render(request, 'shop/newuser.html')

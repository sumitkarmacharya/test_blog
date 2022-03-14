from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        email=request.user.email
    else:
        email=''
    return render(request,'index.html',{'name':'Sumit','email':email})

def about(request):
    return HttpResponse("This is about seciton")
from django.shortcuts import render
# from django.http import HttpResponse
from .models import Experience
from .models import Education
def home(request):
    experience = Experience.objects.all()
    education = Education.objects.all()

    return render(request,'index.html',{'experience' : experience,'Education' : education})

def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    return render(request,'contact.html')
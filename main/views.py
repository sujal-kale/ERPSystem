from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def faculty(request):
    return render(request, 'main/faculty.html')

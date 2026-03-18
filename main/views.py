from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def faculty(request):
    return render(request, 'main/faculty.html')

@login_required(login_url='login')
def landing_page(request):
    return render(request, 'landingpage.html', {'username': request.user.username})

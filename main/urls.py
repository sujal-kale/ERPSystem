from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('faculty/', views.faculty, name='faculty'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
]

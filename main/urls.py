from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('faculty/', views.faculty, name='faculty'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('landing/', views.landing_page, name='landing'),
    path('admin/', admin.site.urls),
]

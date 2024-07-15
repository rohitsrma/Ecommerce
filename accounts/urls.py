from django.contrib import admin
from django.urls import path, include
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
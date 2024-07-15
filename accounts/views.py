from django.shortcuts import render
from django.http import HttpResponse
from accounts.forms import LoginForm

# Create your views here.
def login(request):
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})
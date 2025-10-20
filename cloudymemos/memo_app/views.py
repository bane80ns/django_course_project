from django.shortcuts import render

# Create your views here.

def homepage(request):
    
    return render(request, 'memo_app/index.html')


def register(request):
    
    return render(request, 'memo_app/register.html')


def my_login(request):
    
    return render(request, 'memo_app/my-login.html')


def dashboard(request):
    
    return render(request, 'memo_app/dashboard.html')



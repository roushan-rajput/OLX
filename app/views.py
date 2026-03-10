from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def login(request):     
    return render(request, 'login.html')

def Register(request):
    return render(request, 'Register.html')
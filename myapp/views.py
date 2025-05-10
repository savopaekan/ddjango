from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def departments(request):
    return render(request, 'departments.html')

def cs(request):
    return render(request, 'cs.html')

def biology(request):
    return render(request, 'biology.html')

def history(request):
    return render(request, 'history.html')
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def store(request):
    return render(request, 'store.html')

def about(request):
    return render(request, 'about.html')

def support(request):
    return render(request, 'support.html')

from django.shortcuts import render,redirect
from .forms import RegistroForm
# Create your views here.

def registro(request):   
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('index') 
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})
    

def index(request):
    return render (request,'index.html')
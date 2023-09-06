from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "Something is incorrect, kindly check and login again")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)            
            messages.success(request, "You have been successfully created your account")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})

def customer_detail(request, pk):
    if request.user.is_authenticated:
        customer = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer':customer})
    else:
        messages.success(request, "You must log in...")
        return redirect('home')
    
def customer_delete(request, pk):
    if request.user.is_authenticated:
        customer = Record.objects.get(id=pk)
        customer.delete()
        messages.success(request, "The customer's records has been deleted...")
        return redirect('home')
    else:
        messages.success(request, "You must log in...")
        return redirect('home')
    
def customer_add(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            add_record = form.save()
            messages.success(request, "Record Saved")
            return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You must log in")
        return redirect('home')
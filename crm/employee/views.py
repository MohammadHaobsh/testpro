from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Employee

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username', '')  
        password = request.POST.get('password', '')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  
            else:
                messages.error(request, "Incorrect username or password")
        else:
            messages.error(request, "Please fill in all fields")
    
    return render(request, 'employee/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        if Employee.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = Employee.objects.create_user(username=username, email=email, phone=phone, password=password)
            messages.success(request, 'Account created successfully, you can log in now')
            return redirect('login')

    return render(request, 'employee/register.html')@login_required
def add_employee(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        position = request.POST.get("position")  
        if Employee.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            employee = Employee.objects.create_user(username=username, email=email, phone=phone)
            employee.position = position 
            employee.save()
            messages.success(request, "Employee data added successfully!")
            return redirect("dashboard")

    return render(request, "employee/add_employee.html")

add_employee

@login_required
def dashboard(request):
    employees = Employee.objects.all() 
    return render(request, 'employee/dashboard.html', {'employees': employees})


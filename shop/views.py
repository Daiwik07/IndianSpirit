from django.shortcuts import render, redirect,HttpResponse
from datetime import datetime
from shop.models import Sign
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Sign
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
 
import csv
  
def export_users_csv(request):
    
     
    if request.method == 'POST':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Data.csv"'        
        writer = csv.writer(response)
        writer.writerow(['Employee Detail'])       
                 
         
        writer.writerow(['name','Email','Description','date'])
 
        users = Sign.objects.all().values_list('name','Email','Description','date')
         
        for user in users:
            writer.writerow(user)
        return response
 
    return render(request, 'exportexel.html')

# Create your views here.
def home(request):
    print(request.user)
    return render(request, 'test1.html')

def about(request):
    return render(request, 'about.html')

def uttar(request):
    return render(request, 'uttar.html')

def maha(request):
    return render(request, 'maha.html')

def raja(request):
    return render(request, 'raja.html')

def feedback(request):
        if request.method=="POST":
            Name = request.POST.get('Name')
            Email=request.POST.get('Email')
            Description=request.POST.get('Description')
            context={'name':Name,
                    'desc':Description}
            feedback = Sign(name = Name, Email = Email, Description= Description,date=datetime.today())
            feedback.save()

        return render(request, 'feedback.html')


def loginUser(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST.get('name')
        loginpassword=request.POST.get('password')

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")
    return HttpResponse("404- Not found")

def login_view(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        sign = User.objects.create_user(username = name, password= password)
        sign.save()

    return render(request, 'signup.html')

def logOut(request):
    logout(request)
    return redirect("http://127.0.0.1:8000/")

def map(request):
    return render(request, 'test.html')

def telangana(request):
    return render(request, 'telangana.html',)

def andhra(request):
    return render(request, 'andhra.html')

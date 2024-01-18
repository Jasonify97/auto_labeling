from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

def main(request):
    return render(request, "user/main.html")

def signup(request):
    if request.method == "POST":
        if request.POST['password1']==request.POST['password2']:
            user=User.objects.create_user(request.POST['username'], password=request.POST['password1'], first_name=request.POST['project_name'])
            auth.login(request,user)
            return redirect('http://127.0.0.1:8000/user/')
    return render(request,'user/signup.html')




def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('http://127.0.0.1:8000/workspace/')
        else:
            return render(request,'login.html', {'error':'username or password is incorrect'})
    else:
        return render(request,'user/login.html')
    
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('http://127.0.0.1:8000/user/')
    return render(request,'user/main.html')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *

def index(request):
    user_instance = User.objects.all()
    project_instance = UserProfile.objects.all()


    return render(request, 'workspace/workspace.html', {'work_space': user_instance, 'project_instance': project_instance})

def create_project(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    return render(request, 'workspace/workspace.html')
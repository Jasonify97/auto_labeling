from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *

def index(request):
    user_instance = User.objects.all()
    project_instance = UserProfile.objects.all()

    return render(request, 'workspace/workspace.html', {'work_space': user_instance, 'project_instances': project_instance})

def create_project(request):
    if request.method == 'POST':
        project_name = request.POST['assign_project']
        user_id = request.user.id
        project_save = UserProfile(project_name = project_name, user_name_id = user_id)
        project_save.save()
        
    return redirect("http://127.0.0.1:8000/workspace/")
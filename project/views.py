from django.shortcuts import render, redirect
from .models import *

def upload(request):
    
    return render(request, "project/upload.html")

def annotate(request):
    
    return render(request, "project/annotate.html")

def classes(request):
    
    return render(request, "project/classes.html")

def generate(request):
    
    return render(request, "project/generate.html")


def create_classes(request):
    if request.method == "POST":
        input_classes = request.POST.get('input_classes', '')
        
        input_classes = input_classes.replace(" ","").split(',')

        for name in input_classes:
            class_instance, created = Classes.objects.get_or_create(classes_instance=name)
        
        return redirect('show_classes')
    return render(request, 'project/create_classes.html')

def show_classes(request):
    classes_lists = Classes.objects.all()
    return render(request, 'project/show_classes.html', {'classes_lists': classes_lists})
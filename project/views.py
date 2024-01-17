from django.shortcuts import render
from django.http import HttpResponse

def upload(request):
    
    return render(request, "project/upload.html")

def annotate(request):
    
    return render(request, "project/annotate.html")

def classes(request):
    
    return render(request, "project/classes.html")

def generate(request):
    
    return render(request, "project/generate.html")

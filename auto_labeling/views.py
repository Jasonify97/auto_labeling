import os, secrets
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage()

def main(request):
    return render(request, 'main.html')

def start(request):
    return render(request, 'start.html')

def upload_file(request): # /media에 파일 업로드
    if request.method == 'POST':
        folder_path = os.path.join("media","img")
        for image in request.FILES.getlist('file'):
            destination_path = os.path.join(folder_path, image.name)
            with open(destination_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
        return render(request, 'main.html')
    return HttpResponse('Failed') 


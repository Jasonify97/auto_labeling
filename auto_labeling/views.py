import os, secrets
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage()

def main(request):
    return render(request, 'main.html')

def start(request):
    return render(request, 'start.html')

def upload_file(request): # /media에 파일 업로드     
    if request.method == 'POST' and request.FILES.getlist('file'):
        uploaded_files = request.FILES.getlist('file')
        upload_dir = os.path.join(settings.MEDIA_ROOT, 'img')
        image_paths = []
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        for uploaded_file in uploaded_files:
            file_path = os.path.join(upload_dir, uploaded_file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            image_paths.append(os.path.join(settings.MEDIA_URL, 'img', uploaded_file.name))
        image_paths = [image_path.replace('\\', '/') for image_path in image_paths]
        return render(request, 'main.html', {'image_paths': image_paths})
    return HttpResponse('Failed') 


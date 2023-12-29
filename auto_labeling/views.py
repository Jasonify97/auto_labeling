import os, secrets
from django.http import HttpResponse
from django.shortcuts import render

def token(request): # 토큰 발급
    token = secrets.token_hex()
    os.makedirs(token)
    return HttpResponse('Create Folder Success')

def main(request):
    return render(request, 'main.html')

def start(request):
    return render(request, 'start.html')

def index(request):
    return HttpResponse('Here is Index View!')

# def upload_images(request):
#     if request.method == 'POST':



import os, secrets
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.sessions.models import Session

def main(request):
    return render(request, 'main.html')

def start(request):
    return render(request, 'start.html')

def index(request):
    print(secrets.token_hex())


    return HttpResponse('Here is Index View!')

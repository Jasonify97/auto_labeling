from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def start(request):
    return render(request, 'start.html')

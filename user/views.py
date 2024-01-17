from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Helloworld! here is user view!")

def main(request):
    return render(request, "user/main.html")

def login(request):
    return render(request, "user/login.html")

def signup(request):
    return render(request, "user/signup.html")

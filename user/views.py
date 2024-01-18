from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, "user/main.html")

def login(request):
    return render(request, "user/login.html")

def sign_up(request):
    return render(request, "user/signup.html")

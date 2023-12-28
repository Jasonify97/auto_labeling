from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), # 일단 냄겨둠
    path('folder/', views.token, name='token'),
    path('', views.start, name='start'), #start 페이지로 이동
    path('main/', views.main, name='main'),
]

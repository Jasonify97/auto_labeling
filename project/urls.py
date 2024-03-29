from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),


    path("upload/", views.upload),
    path("annotate/", views.annotate),
    path("classes/", views.classes),
    path("generate/", views.generate),

    path("create_classes/", views.create_classes, name='create_classes'),
    path('show_classes/', views.show_classes, name='show_classes'),

]

from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload),
    path("annotate/", views.annotate),
    path("classes/", views.classes),
    path("generate/", views.generate),
]

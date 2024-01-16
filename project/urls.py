from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload),
    path("annotate/", views.upload),
    path("classes/", views.upload),
    path("generate/", views.upload),
]

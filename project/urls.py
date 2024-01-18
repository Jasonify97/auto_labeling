from django.urls import path
from . import views


app_name = 'project'
urlpatterns = [
    path("upload/",  views.upload, name='upload'),
    path("annotate/", views.annotate_main, name='annotate'),
    path("annotate/work/", views.annotate),
    # path("classes/", views.upload),
    # path("generate/", views.upload),
]

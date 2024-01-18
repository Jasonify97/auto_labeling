from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# urlpatterns = [
#     path('', views.start, name='start'), #start 페이지로 이동
#     path('main/', views.main),
#     path('upload/', views.upload_file, name='upload_file'),
#     path('main/Post_xy_point/', views.Post_xy_point), 
#     path("user/", include("user.urls")),
#     path("workspace/", include("workspace.urls")),
#     path("project/", include("project.urls")),
# ]

urlpatterns = [
    path('project/', include('project.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project_name = models.TextField(blank=True)
    project_create_time = models.TextField(blank=True)
    images_count = models.TextField(blank=True)
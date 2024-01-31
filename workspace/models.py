from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.TextField(blank=True, null=True)


    
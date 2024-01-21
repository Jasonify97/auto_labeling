from django.db import models
from workspace.models import UserProfile

class Classes(models.Model):
    project_name = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    classes_count = models.AutoField(primary_key=True)
    classes_instance = models.CharField(max_length=100)



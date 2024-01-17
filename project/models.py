from django.db import models

# Create your models here.
class Classes(models.Model):
    classes = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
                          

    def set_classes(self, classes):
        self.classes = classes


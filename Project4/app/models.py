from django.db import models

# Create your models here.

class Student(models.Model):
    rollno = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    pno = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cls = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
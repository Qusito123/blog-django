from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to="projects")
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
# Create your models here.

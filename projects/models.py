from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    project_image = models.ImageField(upload_to='project/', blank=True)
    url= models.CharField(max_length=100)

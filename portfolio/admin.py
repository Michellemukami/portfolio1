from django.contrib import admin
from .models import Project

class ImageAdmin(admin.ModelAdmin):
   

    admin.site.register(Project)
  
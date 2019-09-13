from django.shortcuts import render,redirect
from .models import Project
# Create your views here.
def home (request):
    return render(request, 'home.html')
def about (request):
    return render(request, 'about.html')
def project(request):
    
    posts=Project.objects.all()
    return render(request, 'project.html',{"posts":posts})
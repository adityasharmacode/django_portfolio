from django.shortcuts import render

# Create your views here.
from .models import Project

def home(request):
    return render(request, "portfolio/home.html")

def about(request):
    return render(request, "portfolio/about.html")

def projects(request):
    projects = Project.objects.all()
    return render(request, "portfolio/projects.html", {"projects": projects})

def contact(request):
    return render(request, "portfolio/contact.html")

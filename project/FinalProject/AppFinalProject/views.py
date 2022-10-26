from django.shortcuts import render
from AppFinalProject.models import User

def home(request):
    return render(request, "AppFinalProject/home.html")

def posts(request):
        return render(request, "AppFinalProject/posts.html")

def contact(request):
        return render(request, "AppFinalProject/contact.html")

def about(request):
        return render(request, "AppFinalProject/about.html")

def show_users(request):
  users = User.objects.all()
  return render(request, "AppFinalProject/users.html", {"users": users})


# Create your views here.

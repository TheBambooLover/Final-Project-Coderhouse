from django.shortcuts import render

def home(request):
    return render(request, "AppFinalProject/home.html")

def posts(request):
        return render(request, "AppFinalProject/posts.html")

def writters(request):
        return render(request, "AppFinalProject/writters.html")

def about(request):
        return render(request, "AppFinalProject/about.html")


# Create your views here.

from django.shortcuts import render

def home(request):
    return render(request, "AppFinalProject/index.html")

def posts(request):
        return render(request, "AppFinalProject/posts.html")

def conctact(request):
        return render(request, "AppFinalProject/contact.html")

def about(request):
        return render(request, "AppFinalProject/about.html")


# Create your views here.

from django.shortcuts import render
from AppFinalProject.models import User
from AppFinalProject.forms import Buscar
from django.views import View

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

class BuscarUser(View):
    form_class = Buscar
    template_name = 'AppFinalProject/search.html'
    initial = {"Usuario":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            users = User.objects.filter(nombre__icontains=username).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'users':users})
        return render(request, self.template_name, {"form": form})

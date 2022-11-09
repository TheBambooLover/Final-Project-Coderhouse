from tokenize import group
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from AppFinalProject.models import User
from AppFinalProject.forms import Buscar, CommentForm, UserForm,Post, WritterForm
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

@login_required
def home(request):
    return render(request, "AppFinalProject/home.html")

def posts(request):
        return render(request, "AppFinalProject/posts.html")
        
def about(request):
        return render(request, "AppFinalProject/about.html")

def show_writters(request):
    writters = User.objects.filter(writter=True).all()
    return render(request,"AppFinalProject/writters.html",{"writters":writters})

class UsersList(ListView):
    model = User

class BuscarUser(View):
    form_class = Buscar
    template_name = 'AppFinalProject/search.html'
    initial = {"User":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            users = User.objects.filter(username__icontains=username,writter=False).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'users':users})
        return render(request, self.template_name, {"form": form})

class CreateUser(View):
    form_class = UserForm
    template_name = "AppFinalProject/new_user.html"
    initial = {'username':"", 'password':"", 'email':"" , 'writter':""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el usuario {form.cleaned_data.get('username')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class CreateComment(View):
    form_class = CommentForm
    template_name = "AppFinalProject/create_comment.html"
    initial = {'user':"", 'text':"", 'post':""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el comentario para el post {form.cleaned_data.get('post')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class CreateWritter(View):
    form_class = WritterForm
    template_name = "AppFinalProject/new_writter.html"
    initial = {'username':"", 'password':"", 'email':"" ,'writter':1, 'about':""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el escritor {form.cleaned_data.get('username')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ListPosts(ListView):
    model = Post
    template_name="AppFinalProject/posts_list.html"

class DetailPost(DetailView):
    model = Post
    template_name="AppFinalProject/post_detail.html"

class CreatePost(CreateView):
    model = Post
    success_url = "/AppFinalProject/posts"
    fields = ['writter', 'title', 'text', 'image']

class UpdatePost(UpdateView):
    model=Post
    success_url = "/AppFinalProject/posts"
    fields = ['writter', 'title', 'text', 'image']

class DeletePost(DeleteView):
    model = Post
    succes_url = "/AppFinalProject/posts"
class Login(LoginView):
    template_name = 'AppFinalProject/login.html'
    next_page = reverse_lazy("home")

class Logout(LogoutView):
    template_name = 'AppFinalProject/logout.html'

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "AppFinalProject/registration/signup.html"

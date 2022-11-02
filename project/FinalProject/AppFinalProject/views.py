from tokenize import group
from django.shortcuts import render
from AppFinalProject.models import User
from AppFinalProject.forms import Buscar, CommentForm, PostForm, UserForm,Post, WritterForm
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

def show_writters(request):
    writters = User.objects.filter(group_id=3).all()
    return render(request,"AppFinalProject/writters.html",{"writters":writters})

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
            users = User.objects.filter(username__icontains=username,group_id=2).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'users':users})
        return render(request, self.template_name, {"form": form})

class CreateUser(View):
    form_class = UserForm
    template_name = "AppFinalProject/new_user.html"
    initial = {'username':"", 'password':"", 'email':"" , 'group':"2"}

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

class CreatePost(View):
    form_class = PostForm
    template_name = "AppFinalProject/create_post.html"
    initial = {'writter':"", 'title':"", 'text':"" ,'image':""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el artículo {form.cleaned_data.get('title')}"
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
    initial = {'username':"", 'password':"", 'email':"" ,'group':"3", 'about':""}

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
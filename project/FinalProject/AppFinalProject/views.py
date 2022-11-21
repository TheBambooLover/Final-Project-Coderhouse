from tokenize import group
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from AppFinalProject.models import User
from AppFinalProject.forms import Buscar, CommentForm, UserForm,Post, WritterForm, EditProfileForm
from django.views import View
from django.contrib.auth.models import User as UserDjango
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User, Group
from AppFinalProject.models import User
from AppFinalProject.forms import Buscar, CommentForm, UserForm,Post, WritterForm,PasswordChangingForm
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView

class GroupRequiredMixin(object):
    """
        group_required - list of strings, required param
    """

    group_required = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        else:
            user_groups = []
            for group in request.user.groups.values_list('name', flat=True):
                user_groups.append(group)
            if len(set(user_groups).intersection(self.group_required)) <= 0:
                raise PermissionDenied
        return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)

def home(request):
    return render(request, "AppFinalProject/home.html")

@login_required
def posts(request):
        return render(request, "AppFinalProject/posts.html")

@login_required        
def about(request):
        return render(request, "AppFinalProject/about.html")

@login_required
def show_writters(request):
    writters = UserDjango.objects.filter(groups=1).all()
    return render(request,"AppFinalProject/writters.html",{"writters":writters})



@login_required
def Profile(request):
    args = {'user':request.user}
    return render(request, 'AppFinalProject/profile.html',args)


@login_required
def EditProfile(request):

    if request.method=='POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('AppFinalProject/home/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request,'AppFinalProject/user_custom/edit_profile.html',args)    

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

class CreateUser(CreateView):
    form_class = UserForm
    template_name = "AppFinalProject/new_user.html"
    initial = {'username':"", 'password':"", 'email':"" , 'group':"", 'icon':""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            user = User.objects.create_user(username,email,password)
            user.save()
            userGroup = Group.objects.get(name='user')
            user.groups.add(userGroup)
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

class ListPosts(LoginRequiredMixin,ListView):
    model = Post
    template_name="AppFinalProject/posts_list.html"

class DetailPost(LoginRequiredMixin,DetailView):
    model = Post
    template_name="AppFinalProject/post_detail.html"

class CreatePost(LoginRequiredMixin,GroupRequiredMixin,CreateView):

    group_required =[u'admin',u'writter']
    model = Post
    success_url = "/AppFinalProject/posts"
    fields = ['title', 'text', 'image']

    def get_initial(self):
        initial = super(CreatePost, self).get_initial()
        initial.update({'writter': self.request.user.username,
                        'title':"",
                        'text':"",
                        'image':""})
        return initial

    def form_valid(self, form):
        """Force the user to request.user"""
        self.object = form.save(commit=False)
        self.object.writter = self.request.user.username
        self.object.save()

        return super(CreatePost, self).form_valid(form)

class UpdatePost(LoginRequiredMixin,GroupRequiredMixin,UpdateView):
    group_required =[u'admin']
    model=Post
    success_url = "/AppFinalProject/posts"
    fields = ['writter','title', 'text', 'image']

class DeletePost(LoginRequiredMixin,GroupRequiredMixin,DeleteView):
    group_required =[u'admin']
    model = Post
    success_url = "/AppFinalProject/posts"

class Login(LoginView):
    template_name = 'AppFinalProject/login.html'
    next_page = reverse_lazy("home")

class Logout(LogoutView):
    template_name = 'AppFinalProject/home.html'

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "AppFinalProject/registration/signup.html"

class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    login_url = 'login'
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, "AppFinalProject/user_custom/password_change_success.html")
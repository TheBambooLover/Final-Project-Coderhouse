from tokenize import group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.models import User as UserDjango , Group
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from AppFinalProject.models import User
from AppFinalProject.forms import UserForm, Post, EditUserProfileForm , PasswordChangingForm, SignupForm


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


@login_required
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
    return render(request, "AppFinalProject/writters.html", {"writters": writters})


@login_required
def Profile(request):
    args = {'user': request.user}
    return render(request, 'AppFinalProject/profile.html', args)


class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = EditUserProfileForm
    login_url = 'login'
    template_name = "AppFinalProject/user_custom/edit_profile.html"
    success_url = reverse_lazy('home')
    success_message = "User updated"

    def get_object(slef):
        return slef.request.user

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
                             "Please submit the form carefully")
        return redirect('home')


class CreateUser(CreateView):
    form_class = UserForm
    template_name = "AppFinalProject/new_user.html"
    initial = {'username': "", 'password': "", 'email': "", 'group': ""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username, email, password)
            user.save()
            userGroup = Group.objects.get(name='user')
            user.groups.add(userGroup)
            msg_exito = f"se cargo con éxito el usuario {form.cleaned_data.get('username')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form,
                                                        'msg_exito': msg_exito})

        return render(request, self.template_name, {"form": form})


class ListPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = "AppFinalProject/posts_list.html"


class DetailPost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "AppFinalProject/post_detail.html"


class CreatePost(LoginRequiredMixin, GroupRequiredMixin, CreateView):

    group_required = [u'admin', u'writter']
    model = Post
    success_url = "/AppFinalProject/posts"
    fields = ['title', 'text', 'image']

    def get_initial(self):
        initial = super(CreatePost, self).get_initial()
        initial.update({'writter': self.request.user.get_username(),
                        'title': "",
                        'text': "",
                        'image': ""})
        return initial

    def form_valid(self, form):
        """Force the user to request.user"""
        self.object = form.save(commit=False)
        self.object.writter = self.request.user.get_username()
        self.object.save()

        return super(CreatePost, self).form_valid(form)


class UpdatePost(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    group_required = [u'admin']
    model = Post
    success_url = "/AppFinalProject/posts"
    fields = ['writter', 'title', 'text', 'image']


class DeletePost(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    group_required = [u'admin']
    model = Post
    success_url = "/AppFinalProject/posts"


class Login(LoginView):
    template_name = 'AppFinalProject/login.html'
    next_page = reverse_lazy("home")


class Logout(LogoutView):
    template_name = 'AppFinalProject/logout.html'


class SignUp(SuccessMessageMixin, CreateView):
    form_class = SignupForm
    template_name = "AppFinalProject/registration/signup.html"
    success_url = reverse_lazy('login')
    success_message = "User has been created, please login with your username and password"

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
                             "Please enter details properly")
        return redirect('home')


class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    login_url = 'login'
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, "AppFinalProject/user_custom/password_change_success.html")

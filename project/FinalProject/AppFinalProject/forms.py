from dataclasses import fields
from django import forms
from AppFinalProject.models import Post, User, Comment
from django.forms import Textarea
from django.contrib.auth.models import User as UserDjango
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm

class Buscar(forms.Form):
  username = forms.CharField(max_length=100)

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password', 'email','icon']

class WritterForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password', 'email','about','icon','writter']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['user', 'text', 'post']

class PostForm(forms.ModelForm):
  text = forms.CharField(widget=Textarea(attrs={'class': 'form-control', 'rows': '4', 'cols': '10'}))

  class Meta:
    model = Post
    fields = ['writter', 'title', 'text', 'image']

class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = UserDjango
        fields = (
          'email',
          'username',
          'first_name',
          'last_name',
          )

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Passowrd'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Conform new password'}))
    class Meta:
        model = UserDjango
        fields = ['old_password', 'new_password1', 'new_password2']
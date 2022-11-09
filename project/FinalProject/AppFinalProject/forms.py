from dataclasses import fields
from django import forms
from AppFinalProject.models import Post, User, Comment

class Buscar(forms.Form):
  username = forms.CharField(max_length=100)

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password', 'email']

class WritterForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password', 'email','about','icon','writter']

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['writter', 'title', 'text', 'image']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['user', 'text', 'post']

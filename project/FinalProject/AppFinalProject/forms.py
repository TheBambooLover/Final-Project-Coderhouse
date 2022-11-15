from dataclasses import fields
from django import forms
from AppFinalProject.models import Post, User, Comment
from django.forms import Textarea

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

from dataclasses import fields
from django import forms
from AppFinalProject.models import Post, User
from django.forms import Textarea
from django.contrib.auth.models import User as UserDjango
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm

class Buscar(forms.Form):
  username = forms.CharField(max_length=100)

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password', 'email']

class WritterForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password', 'email','about','writter']

class PostForm(forms.ModelForm):
  text = forms.CharField(widget=Textarea(attrs={'class': 'form-control', 'rows': '4', 'cols': '10'}))

  class Meta:
    model = Post
    fields = ['writter', 'title', 'text', 'image']

class EditUserProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter your email"}))
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your first name"}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your last name"}))

    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your username"}))
    
    password = None
    class Meta:
        model = UserDjango
        fields = (
          'username', 'first_name', "last_name", 'email'
          )

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Passowrd'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Conform new password'}))
    class Meta:
        model = UserDjango
        fields = (
          'old_password',
          'new_password1',
          'new_password2',
          )

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your email-id'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserDjango
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
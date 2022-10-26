from tkinter import CASCADE
from unittest.mock import DEFAULT
from certifi import where
from django.db import models

class Groups(models.Model):
    group = models.CharField(max_length=30)

class User(models.Model):
    username = models.CharField(max_length=18)
    password = models.CharField(max_length=22)
    email = models.CharField(max_length=300)
    icon = models.CharField(max_length=300, default="placeholder.jpg")
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)

class Post(models.Model):
    writter = models.ForeignKey(User, on_delete=models.CASCADE)
    votes=models.IntegerField()
    text=models.CharField(max_length=300)
    image=models.CharField(max_length=300, null=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=0)

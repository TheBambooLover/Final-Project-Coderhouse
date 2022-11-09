from email.policy import default
from tkinter import CASCADE
from unittest.mock import DEFAULT
from unittest.util import _MAX_LENGTH
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=18)
    password = models.CharField(max_length=22)
    email = models.CharField(max_length=300)
    icon = models.ImageField(upload_to="usersicons", default="placeholder.jpg")
    about = models.CharField(max_length=500, null=True)
    writter = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.username}"

class Post(models.Model):
    writter = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    text=models.CharField(max_length=300)
    image=models.ImageField(upload_to="posts", null=True)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f"{self.text}"

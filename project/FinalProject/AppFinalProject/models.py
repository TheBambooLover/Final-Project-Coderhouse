from email.policy import default
from tkinter import CASCADE
from unittest.mock import DEFAULT
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import date

class User(models.Model):
    username = models.CharField(max_length=18, unique=True)
    password = models.CharField(max_length=22)
    email = models.CharField(max_length=300, unique=True)
    about = models.CharField(max_length=500, null=True)
    writter = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.username}"

class Post(models.Model):
    writter = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text=models.TextField(max_length=30000)
    image=models.ImageField(upload_to="djangouploads/postuploads/images", null=True)
    posted_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
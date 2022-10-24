from django.urls import path
from AppFinalProject import views

urlpatterns = [
    path('index/',views.home,name='index'),
    path('posts/',views.posts,name='posts'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),

]

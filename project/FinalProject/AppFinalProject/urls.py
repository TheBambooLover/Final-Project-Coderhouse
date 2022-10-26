from django.urls import path
from AppFinalProject import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('posts/',views.posts,name='posts'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('users/',views.show_users),

]

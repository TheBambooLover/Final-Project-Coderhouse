from django.urls import path
from AppFinalProject import views

urlpatterns = [
    path('home/',views.home),
    path('posts/',views.posts),
    path('writters/',views.writters),
    path('about/',views.about),

]

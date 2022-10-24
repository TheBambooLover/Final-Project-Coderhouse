from django.urls import path
from AppFinalProject import views

urlpatterns = [
    path('index/',views.home),
    path('posts/',views.posts),
    path('contact/',views.conctact),
    path('about/',views.about),

]

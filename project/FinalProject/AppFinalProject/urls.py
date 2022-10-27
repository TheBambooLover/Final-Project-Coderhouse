from lib2to3.pygram import pattern_grammar
from django.urls import path
from AppFinalProject import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('posts/',views.posts,name='posts'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('users/',views.show_users),
    path('users-search',views.BuscarUser.as_view()),
    path('user-create',views.AltaUser.as_view()),

]

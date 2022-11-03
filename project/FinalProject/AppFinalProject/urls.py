from lib2to3.pygram import pattern_grammar
from django.urls import path
from AppFinalProject import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('posts/',views.posts,name='posts'), #all posts
    path('about/',views.about,name='about'),
    path('writters',views.show_writters,name='writters'),
    path('users/',views.show_users),
    path('search-users',views.BuscarUser.as_view()),
    path('create-user',views.CreateUser.as_view()),
    path('create-post',views.CreatePost.as_view()),
    path('create-comment',views.CreateComment.as_view()),
    path('create-writter',views.CreateWritter.as_view()),
    path('writters',views.show_writters,name='writters'),

]

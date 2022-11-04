from lib2to3.pygram import pattern_grammar
from django.urls import path
from AppFinalProject import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('writters',views.show_writters,name='writters'),
    path('users/',views.show_users),
    path('search-users',views.BuscarUser.as_view()),
    path('create-user',views.CreateUser.as_view()),
    #path('create-post',views.CreatePost.as_view()),
    path('create-comment',views.CreateComment.as_view()),
    path('create-writter',views.CreateWritter.as_view()),
    path('writters',views.show_writters,name='writters'),
    path('posts', views.ListPosts.as_view(), name='Posts'),
    path(r'^(?P<pk>\d+)$', views.DetailPost.as_view(), name="Detail"),
    path(r'^new$',views.CreatePost.as_view(), name='New'),
    path(r'^edit/(?P<pk>\d+)$',views.UpdatePost.as_view(), name='Edit'),
    path(r'^delete/(?P<pk>\d+)$',views.DeletePost.as_view(), name='Delete'),

]

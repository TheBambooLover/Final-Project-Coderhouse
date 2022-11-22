from lib2to3.pygram import pattern_grammar
from django.urls import path
from AppFinalProject import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),    
    path('logout',views.Logout.as_view(),name='logout'),
    path('writters/',views.show_writters,name='writters'),
    path('search-users',views.BuscarUser.as_view()),
    path('create-user',views.CreateUser.as_view()),
    path('create-comment',views.CreateComment.as_view()),
    path('create-writter',views.CreateWritter.as_view()),
    path('writters',views.show_writters,name='writters'),
    path('posts', views.ListPosts.as_view(), name='Posts'),
    path(r'^(?P<pk>\d+)$', views.DetailPost.as_view(), name="Detail"),
    path(r'^new$',views.CreatePost.as_view(), name='New'),
    path(r'^edit/(?P<pk>\d+)$',views.UpdatePost.as_view(), name='Edit'),
    path(r'^delete/(?P<pk>\d+)$',views.DeletePost.as_view(), name='Delete'),
    path('login',views.Login.as_view(),name='login'),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path(r'^profile/$',views.Profile, name='profile'),
    path(r'^profile/edit/$',views.UpdateUserView.as_view(), name='edit_profile'),
    path(r'^profile/edit/password/$',views.PasswordChangeView.as_view(template_name="AppFinalProject/user_custom/password_change.html"),
    name='edit_password'),
    path(r'^profile/edit/password_success/$',views.password_success,name='password_success'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
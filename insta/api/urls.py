
# filepath: /C:/Users/death/Desktop/deepsolv/api/urls.py
from django.urls import path
from .views import hello_world
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('', views.homepage, name='homepage'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('post/<uuid:post_id>/', views.post_detail, name='post_detail'),
    path('profile/<str:username>/follow/', views.follow, name='follow'),
    path('profile/<str:username>/unfollow/', views.unfollow, name='unfollow'),
    path('post/<uuid:post_id>/likes/', views.post_likes, name='post_likes'),
]

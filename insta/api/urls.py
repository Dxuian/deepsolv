
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
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.homepage, name='homepage'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('post/<uuid:post_id>/', views.post_detail, name='post_detail'),
    path('post/<uuid:post_id>/likes/', views.post_likes, name='post_likes'),
]

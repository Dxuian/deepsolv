from django.shortcuts import render

# Create your views here.
# filepath: /C:/Users/death/Desktop/deepsolv/api/views.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Post
from django.core.paginator import Paginator


 


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def homepage_view(request):
    posts = Post.objects.filter(user__in=request.user.following.all()).order_by('-when_posted')
    paginator = Paginator(posts, 10)   
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'homepage.html', {'page_obj': page_obj})

@login_required
def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = profile_user.posts.all().order_by('-when_posted')
    return render(request, 'profile.html', {'profile_user': profile_user, 'posts': posts})

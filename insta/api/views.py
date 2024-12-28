from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator
from django.http import HttpResponse



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import Post, User, Likes, Follows
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm, PostForm
from .models import Post, User, Likes, Follows
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.
# filepath: /C:/Users/death/Desktop/deepsolv/api/views.py

def hello_world(request):
    return HttpResponse("Hello, World!")



 

DEV = True
def PASSWORDLENGTH():
    if(DEV):
        return 0 
    return 8
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            email_confirmation = form.cleaned_data['email_confirmation']
            password = form.cleaned_data['password']
            password_confirmation = form.cleaned_data['password_confirmation']
            accept_terms = form.cleaned_data['accept_terms']

            # Validate if passwords match
            if password != password_confirmation:
                messages.error(request, "Passwords do not match.")
                return render(request, "register.html", {"form": form})

            # Validate if emails match
            if email != email_confirmation:
                messages.error(request, "Emails do not match.")
                return render(request, "register.html", {"form": form})

            # Validate password strength (min 8 characters)
            if len(password) < PASSWORDLENGTH():
                messages.error(request, "Password must be at least 8 characters long.")
                return render(request, "register.html", {"form": form})

            # Check if username or email is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken.")
                return render(request, "register.html", {"form": form})

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered.")
                return render(request, "register.html", {"form": form})

            # Create the user
            user = User.objects.create_user(username=username, password=password, email=email)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # Success message
            messages.success(request, "Account created successfully!")
            return redirect('login')  # Redirect to login page after successful registration

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib import messages



from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, PostCaption
import uuid
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post, Comment, Follows, Likes
from django.core.paginator import Paginator
from django.contrib import messages
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            # Validation in view (check if the fields are not empty)
            if not username or not password:
                messages.error(request, "Username and password cannot be empty.")
                return render(request, "login.html", {"form": form})

            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("homepage")
            else:
                messages.error(request, "Invalid username or password.")
                return render(request, "login.html", {"form": form})
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, "login.html", {"form": form})

    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post, Comment, Follows, Likes
from django.core.paginator import Paginator
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post, Follows, User
from django.core.paginator import Paginator
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post, Follows, User
from django.core.paginator import Paginator
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post, Follows, User
from django.core.paginator import Paginator
from django.contrib import messages

@login_required
def homepage(request):
    # Get the posts of the users followed by the logged-in user
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            caption = form.cleaned_data["caption"]
            image_or_video_url = form.cleaned_data["image_or_video_url"]
            category = form.cleaned_data["category"]
            location = form.cleaned_data["location"]
            title = form.cleaned_data["title"]

            post_caption = PostCaption.objects.create(content=caption)
            Post.objects.create(
                user=request.user,
                caption=post_caption,
                image_or_video_url=image_or_video_url,
                category=category,
                title=title,
                location=location
            )
            messages.success(request, "Post created successfully!")
            return redirect("homepage")
    form = PostForm()
    followed_users = Follows.objects.filter(follower=request.user).values_list('followed', flat=True)
    followed_posts = Post.objects.filter(user_id__in=followed_users).order_by('-when_posted')[:7]

    # Get the posts from users not followed by the logged-in user (global posts)
    all_users = User.objects.exclude(id=request.user.id)  # Exclude the logged-in user
    non_followed_users = all_users.exclude(id__in=followed_users)
    global_posts = Post.objects.filter(user_id__in=non_followed_users).order_by('-when_posted')[:3]

    # Include posts by the logged-in user (their own posts)
    user_posts = Post.objects.filter(user=request.user).order_by('-when_posted')[:10]

    # Combine the posts: 7 followed posts, 3 non-followed posts, and the user's own posts
    all_posts = list(followed_posts) + list(global_posts) + list(user_posts)

    # Paginate the posts
    paginator = Paginator(all_posts, 10)  # 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Handle post creation
    

    # Get the last 3 comments for each post
    posts_with_comments = []
    for post in page_obj:
        comments = post.comments.all().order_by('-created_at')[:3]
        posts_with_comments.append({'post': post, 'comments': comments})

    return render(request, "homepage.html", {
        "form": form,
        "posts": posts_with_comments,
        "page_obj": page_obj,
    })


@login_required
def profile(request, username):
    user = request.user
    posts = Post.objects.filter(user=user).order_by('-when_posted')

    # Paginate the posts (last 10)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Handle post creation
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            caption = form.cleaned_data["caption"]
            image_or_video_url = form.cleaned_data["image_or_video_url"]
            category = form.cleaned_data["category"]
            location = form.cleaned_data["location"]

            post_caption = PostCaption.objects.create(content=caption)
            Post.objects.create(
                user=user,
                caption=post_caption,
                image_or_video_url=image_or_video_url,
                category=category,
                location=location
            )
            messages.success(request, "Post created successfully!")
            return redirect("profile", username=username)
    else:
        form = PostForm()

    return render(request, "profile.html", {"form": form, "username": username, "page_obj": page_obj})


@login_required
def post_detail(request, post_id):
    post = Post.objects.get(post_id=post_id)

    # Get all comments for this post
    comments = post.comments.all().order_by('-created_at')

    # Handle comment submission
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Comment.objects.create(post=post, user=request.user, content=content)
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {"post": post, "comments": comments, "form": form})


@login_required
def post_likes(request, post_id):
    post = Post.objects.get(post_id=post_id)
    likes = post.likes.all()

    return render(request, 'post_likes.html', {"post": post, "likes": likes})
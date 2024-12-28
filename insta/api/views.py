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

def hello_world(request):
    return HttpResponse("Hello, World!")


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
 

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

            if password != password_confirmation:
                messages.error(request, "Passwords do not match.")
                return render(request, "register.html", {"form": form})

            if email != email_confirmation:
                messages.error(request, "Emails do not match.")
                return render(request, "register.html", {"form": form})

            if len(password) < PASSWORDLENGTH():
                messages.error(request, "Password must be at least 8 characters long.")
                return render(request, "register.html", {"form": form})

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken.")
                return render(request, "register.html", {"form": form})

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered.")
                return render(request, "register.html", {"form": form})

            user = User.objects.create_user(username=username, password=password, email=email)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            messages.success(request, "Account created successfully!")
            return redirect('login')   

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
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post, Follows, Comment
from .forms import PostForm
from .models import Comment  
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post, Likes as Like


@login_required
def homepage(request):
    if request.method == "POST":
        if "create_post" in request.POST:
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
        
        if "create_comment" in request.POST:
            post_id = request.POST.get("post_id")
            content = request.POST.get("content")
            post = Post.objects.get(post_id=post_id)
            Comment.objects.create(post=post, user=request.user, content=content)
            messages.success(request, "Comment added successfully!")
            return redirect("homepage")
        
        if "add_like" in request.POST:
            post_id = request.POST.get("post_id")
            post = Post.objects.get(post_id=post_id)
            
            if post.user == request.user:
                messages.error(request, "You cannot like your own post.")
            else:
                Like.objects.get_or_create(user=request.user, post=post)
                messages.success(request, "Post liked successfully!")
            
            return redirect("homepage")

    form = PostForm()
    followed_users = Follows.objects.filter(follower=request.user).values_list('followed', flat=True)
    followed_posts = Post.objects.filter(user_id__in=followed_users).order_by('-when_posted')[:7]

    all_users = userget.objects.exclude(id=request.user.id)   
    non_followed_users = all_users.exclude(id__in=followed_users)
    global_posts = Post.objects.filter(user_id__in=non_followed_users).order_by('-when_posted')[:3]

    user_posts = Post.objects.filter(user=request.user).order_by('-when_posted')[:10]

    all_posts = list(followed_posts) + list(global_posts) + list(user_posts)

    paginator = Paginator(all_posts, 10)   
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    posts_with_comments = []
    for post in page_obj:
        liked_by_user = Like.objects.filter(user=request.user, post=post).exists()
        
        comments = post.comments.all().order_by('-created_at')[:3]
        posts_with_comments.append({'post': post, 'comments': comments, 'liked_by_user': liked_by_user})

    return render(request, "homepage.html", {
        "form": form,
        "posts": posts_with_comments,
        "page_obj": page_obj
    })




from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Post, Follows
from django.contrib import messages

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .models import Post, Follows
from django.contrib import messages
from django.core.paginator import Paginator

userget = get_user_model()   

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post, Follows

userget = get_user_model()

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post, Follows

userget = get_user_model()

def profile(request, username):
    """
    Display the profile page of a user with their posts and follow/unfollow functionality.
    """
    profile_user = get_object_or_404(userget, username=username)
    
    posts = Post.objects.filter(user=profile_user).order_by('-when_posted')
    
    is_following = Follows.objects.filter(follower=request.user, followed=profile_user).exists()
    
    if request.method == "POST" and request.user.is_authenticated:
        if 'follow' in request.POST:
            if not is_following:
                Follows.objects.create(follower=request.user, followed=profile_user)
                messages.success(request, f"You are now following {profile_user.username}.")
        elif 'unfollow' in request.POST:
            if is_following:
                Follows.objects.filter(follower=request.user, followed=profile_user).delete()
                messages.success(request, f"You have unfollowed {profile_user.username}.")
        
        return redirect('profile', username=username)
    
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "profile.html", {
        "username": username,
        "page_obj": page_obj,
        "user": profile_user,
        "is_following": is_following,
    })



@login_required
def post_detail(request, post_id):
    post = Post.objects.get(post_id=post_id)

    comments = post.comments.all().order_by('-created_at')

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

    if request.method == "POST":
        if post.user == request.user:
            messages.error(request, "You cannot like your own post.")
            return redirect("post_likes", post_id=post_id)

        Likes.objects.create(user=request.user, post=post)
        messages.success(request, "Post liked successfully!")
        return redirect("post_likes", post_id=post_id)
    
    likes = post.likes.all()

    return render(request, 'post_likes.html', {
        "post": post,
        "likes": likes,
        "message": "No likes yet." if likes.count() == 0 else None
    })





from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Follows

userget = get_user_model()

@login_required
def follow(request, username):
    """
    Allows the logged-in user to follow another user.
    """
    if request.user.is_authenticated:
        user_to_follow = get_object_or_404(userget, username=username)

        if user_to_follow != request.user:
            Follows.objects.get_or_create(follower=request.user, followed=user_to_follow)

        return redirect('profile', username=username)
    
    return redirect('login')

@login_required
def unfollow(request, username):
    """
    Allows the logged-in user to unfollow another user.
    """
    if request.user.is_authenticated:
        user_to_unfollow = get_object_or_404(User, username=username)

        if user_to_unfollow != request.user:
            Follows.objects.filter(follower=request.user, followed=user_to_unfollow).delete()

        return redirect('profile', username=username)
    
    return redirect('login')




def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            if not username or not password:
                messages.error(request, "Username and password cannot be empty.")
                return render(request, "login.html", {"form": form})

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
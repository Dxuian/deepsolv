from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
 
    # profile_picture = models.URLField(blank=True, null=True)
class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)

class PostCaption(models.Model):
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    content = models.TextField()

    def __str__(self):
        return f"Caption for Post {self.post_id}"

class Post(models.Model):
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    when_posted = models.DateTimeField(auto_now_add=True)
    caption = models.ForeignKey(PostCaption, on_delete=models.CASCADE)
    image_or_video_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100)  
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Post by {self.user.username} at {self.when_posted}"

class Follows(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    # followed_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    # liked_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} liked Post {self.post.post_id}"
 

 













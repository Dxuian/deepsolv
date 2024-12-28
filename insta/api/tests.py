from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, PostCaption, Follows, Likes, Comment
from django.utils import timezone

User = get_user_model()

class SocialMediaAppTests(TestCase):
    
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1', password='password1', bio="user 1's bio"
        )
        self.user2 = User.objects.create_user(
            username='user2', password='password2', bio="user 2's bio"
        )
        
        self.caption = PostCaption.objects.create(content="this is a post caption")
        
        self.post = Post.objects.create(
            user=self.user1,
            title="post title",
            caption=self.caption,
            category="lifestyle"
        )
        
        self.comment = Comment.objects.create(
            post=self.post,
            user=self.user2,
            content="this is a comment"
        )
        
        self.follow = Follows.objects.create(follower=self.user1, followed=self.user2)

        self.like = Likes.objects.create(user=self.user1, post=self.post)

    def test_user_creation(self):
        self.assertEqual(self.user1.username, 'user1')
        self.assertEqual(self.user2.bio, "user 2's bio")

    def test_post_creation(self):
        self.assertEqual(self.post.user, self.user1)
        self.assertEqual(self.post.title, "post title")
        self.assertEqual(self.post.caption.content, "this is a post caption")
        self.assertEqual(self.post.category, "lifestyle")
    
    def test_follow_functionality(self):
        self.assertEqual(self.follow.follower, self.user1)
        self.assertEqual(self.follow.followed, self.user2)

    def test_like_functionality(self):
        self.assertEqual(self.like.user, self.user1)
        self.assertEqual(self.like.post, self.post)

    def test_comment_creation(self):
        self.assertEqual(self.comment.user, self.user2)
        self.assertEqual(self.comment.content, "this is a comment")
        self.assertEqual(self.comment.post, self.post)

    def test_post_str_representation(self):
        self.assertEqual(str(self.post), f"Post by {self.user1.username} at {self.post.when_posted}")

    def test_caption_str_representation(self):
        self.assertEqual(str(self.caption), f"Caption for Post {self.caption.post_id}")

    def test_follows_str_representation(self):
        self.assertEqual(str(self.follow), f"{self.user1.username} follows {self.user2.username}")

    def test_likes_str_representation(self):
        self.assertEqual(str(self.like), f"{self.user1.username} liked Post {self.post.post_id}")

    def test_comment_str_representation(self):
        self.assertEqual(str(self.comment), f"Comment by {self.user2.username} on Post {self.post.post_id}")

    def test_user_post_relationship(self):
        self.assertIn(self.post, self.user1.posts.all())

    def test_user_comment_relationship(self):
        self.assertIn(self.comment, self.user2.comments.all())

    def test_user_following_relationship(self):
        self.assertIn(self.user2, self.user1.following.all())

    def test_user_follower_relationship(self):
        self.assertIn(self.user1, self.user2.followers.all())

    def test_post_likes(self):
        self.assertIn(self.like, self.post.likes.all())

    def test_comment_creation_time(self):
        self.assertTrue(self.comment.created_at <= timezone.now())

    def test_post_caption_association(self):
        self.assertEqual(self.post.caption, self.caption)
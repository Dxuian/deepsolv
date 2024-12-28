from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import PostCaption, Post, Follows, Likes

User = get_user_model()

class usermodeltest(TestCase):
    def setup(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def testusercreation(self):
        self.assertEqual(self.user.username, 'testuser')

class postcaptionmodeltest(TestCase):
    def setup(self):
        self.caption = PostCaption.objects.create(content='This is a test caption')

    def testcaptioncreation(self):
        self.assertEqual(self.caption.content, 'This is a test caption')

class postmodeltest(TestCase):
    def setup(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.caption = PostCaption.objects.create(content='This is a test caption')
        self.post = Post.objects.create(user=self.user, caption=self.caption, category='test', location='test location')

    def testpostcreation(self):
        self.assertEqual(self.post.user.username, 'testuser')
        self.assertEqual(self.post.caption.content, 'This is a test caption')
        self.assertEqual(self.post.category, 'test')
        self.assertEqual(self.post.location, 'test location')

class followsmodeltest(TestCase):
    def setup(self):
        self.user1 = User.objects.create_user(username='follower', password='12345')
        self.user2 = User.objects.create_user(username='followed', password='12345')
        self.follow = Follows.objects.create(follower=self.user1, followed=self.user2)

    def testfollowcreation(self):
        self.assertEqual(self.follow.follower.username, 'follower')
        self.assertEqual(self.follow.followed.username, 'followed')

class likesmodeltest(TestCase):
    def setup(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.caption = PostCaption.objects.create(content='This is a test caption')
        self.post = Post.objects.create(user=self.user, caption=self.caption, category='test', location='test location')
        self.like = Likes.objects.create(user=self.user, post=self.post)

    def testlikecreation(self):
        self.assertEqual(self.like.user.username, 'testuser')
        self.assertEqual(self.like.post.caption.content, 'This is a test caption')
from django import forms
from .models import Post, PostCaption

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'image_or_video_url', 'category', 'location']
        widgets = {
            'category': forms.TextInput(attrs={'placeholder': 'Enter category'}),
        }

class PostCaptionForm(forms.ModelForm):
    class Meta:
        model = PostCaption
        fields = ['content']

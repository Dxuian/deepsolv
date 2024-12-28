from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'mt-1 w-full rounded-md border-gray-200 p-1.5 bg-white text-sm text-gray-700 shadow-sm',
        'placeholder': 'First Name'
    }))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'mt-1 w-full rounded-md border-gray-200 p-1.5 bg-white text-sm text-gray-700 shadow-sm',
        'placeholder': 'Username'
    }))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'mt-1 w-full rounded-md border-gray-200 p-1.5 bg-white text-sm text-gray-700 shadow-sm',
        'placeholder': 'Last Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'mt-1 w-full rounded-md border-gray-200 p-1.5 bg-white text-sm text-gray-700 shadow-sm',
        'placeholder': 'Email Address'
    }))
    email_confirmation = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'mt-1 w-full rounded-md border-gray-200 p-1.5 bg-white text-sm text-gray-700 shadow-sm',
        'placeholder': 'Confirm Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'mt-1 w-full rounded-md border-gray-200 p-1.5 bg-white text-sm text-gray-700 shadow-sm',
        'placeholder': 'Password'
    }))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'mt-1 w-full rounded-md border-gray-200 p-1.5 bg-white text-sm text-gray-700 shadow-sm',
        'placeholder': 'Confirm Password'
    }))
    accept_terms = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'h-5 w-5 rounded-md border-gray-200 p-1.5 bg-white shadow-sm'
    }))


from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'mt-1 w-full rounded-md border-gray-200 p-1.5 bg-white text-sm text-gray-700 shadow-sm',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'mt-1 w-full rounded-md border-gray-200 p-1.5 bg-white text-sm text-gray-700 shadow-sm',
        'placeholder': 'Password'
    }))



from django import forms

from django import forms
from .models import Comment, Post
class PostForm(forms.Form):
    caption = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'mt-1 w-full rounded-md border-gray-200 p-1.5 bg-white text-sm text-gray-700 shadow-sm',
        'placeholder': 'Enter caption for your post'
    }))
    image_or_video_url = forms.URLField(widget=forms.URLInput(attrs={
        'class': 'mt-1 w-full rounded-md border-gray-200 p-1.5 bg-white text-sm text-gray-700 shadow-sm',
        'placeholder': 'Image or Video URL (optional)'
    }), required=False)
    category = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'mt-1 w-full rounded-md border-gray-200 p-1.5 bg-white text-sm text-gray-700 shadow-sm',
        'placeholder': 'Category'
    }))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'mt-1 w-full rounded-md border-gray-200 p-1.5 bg-white text-sm text-gray-700 shadow-sm',
        'placeholder': 'Location (optional)'
    }), required=False)



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a comment...'})
        }


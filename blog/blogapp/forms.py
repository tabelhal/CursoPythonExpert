from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

class CommentForm(forms.ModelForm):  # ✅ Fixed name
    class Meta:
        model = Comment
        fields = ['text']

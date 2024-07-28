from django import forms
from .models import Author, Post, Comment

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'text']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Buscar')

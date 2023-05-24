from django import forms
from taggit.forms import TagWidget
from .models import Comment, Post


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class SearchForm(forms.Form):
    query = forms.CharField()

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'body', 'publish', 'status', 'tags']
        widgets = {
            'tags': TagWidget(),
        }
        #fields = ['title', 'slug', 'body', 'image', 'category', 'tags']

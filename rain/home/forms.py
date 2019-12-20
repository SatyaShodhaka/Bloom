from django import forms
from django.db import models
from .models import Feedback

class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'article',
            'image',
        )
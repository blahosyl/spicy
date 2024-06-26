from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    The comment form on the recipe detail pages
    """
    class Meta:
        model = Comment
        fields = ('body',)

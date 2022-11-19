from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','img','file','category','caption')
        widgets = {
            "caption": forms.Textarea,

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            "content":forms.Textarea(attrs={
                'placeholder': 'Join the discussion and leave a comment!',
                'class':'form-control','rows':'4'
            }),
        }
        

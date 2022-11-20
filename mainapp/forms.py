from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','img','file','category','caption')
        widgets = {
            "title": forms.TextInput(attrs={
                'placeholder': '프로젝트 제목을 작성해주세요',
            }),

            "category": forms.Select(attrs={
                'class': 'form-control',
                'rows': '1'
            }),


            "content":forms.Textarea(attrs={
                'placeholder': '프로젝트 내용을 작성해주세요',
                'class': 'form-control', 'rows': '10'
            }),

            "caption": forms.Textarea(attrs={
                'placeholder': '"#태그" 형식으로 작성해주세요',
                'class': 'form-control', 'rows': '1'
            }),


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
        

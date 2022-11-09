from django import forms

from .models import User
from django.contrib.auth.forms import UserCreationForm

class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'studentNo', 'password1',"password2",]
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': '이메일'
                }),
            'name': forms.TextInput(attrs={
                'placeholder': '이름'
                }),
            'studentNo': forms.TextInput(attrs={
                'placeholder': '학번'
                }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': '영문, 숫자, 특수문자로 구성된 6~20자 비밀번호'
                }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': '비밀번호 재입력'
                }),
            
        }

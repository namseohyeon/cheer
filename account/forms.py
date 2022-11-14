from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'studentNo', 'password1', "password2"]
        widgets = {
            'email': forms.EmailInput(attrs={
                'id':'username',
                'placeholder': '학교 인증된 이메일을 사용해주세요',
                'class': 'form-control',
                }),
            'name': forms.TextInput(attrs={
                'placeholder': '이름을 입력해주세요',
                'class': 'form-control'
                }),
            'studentNo': forms.TextInput(attrs={
                'placeholder': '학번을 입력해주세요',
                'class': 'form-control'
                }),
            'password1': forms.PasswordInput(attrs={
                'id':'password1',
                'placeholder': '영문, 숫자, 특수문자로 구성된 6~20자 비밀번호를 입력해주세요',
                'class': 'form-control',
                'required': 'required'
                }),
            'password2': forms.PasswordInput(attrs={
                'id':'password2',
                'placeholder': '비밀번호 인증을 위해 재입력해주세요',
                'class': 'form-control',
                'required': 'required'
                }),
            
        }

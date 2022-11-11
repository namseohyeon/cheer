from django.db import models
from account.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    Tag = models.IntegerField(2)
    categoty = models.IntegerField(2)
    img = models.ImageField(blank=True, null=True, upload_to='cheer_photo/%y/%m/%d/')
    file = models.FileField(blank=True, null=True, upload_to='cheer_file/%y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(Account,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user}::{self.content}'

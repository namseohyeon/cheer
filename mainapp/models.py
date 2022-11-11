from django.db import models
from account.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return f'mainapp/category/{self.slug}/'

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    Tag = models.IntegerField(2)
    img = models.ImageField(blank=True, null=True, upload_to='cheer_photo/%y/%m/%d/')
    file = models.FileField(blank=True, null=True, upload_to='cheer_file/%y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    # user = models.ForeignKey(Account,on_delete=models.CASCADE)
    

    scrap = models.ManyToManyField(User, blank=True, related_name='scrap_name')
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user}::{self.content}'

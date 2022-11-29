from django.db import models
from account.models import User
import re
# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=10)
    # slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self) : 
        return self.name
    
    def get_absolute_url(self):
        return f'/mainapp/tag/{self.name}/'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return f'/mainapp/category/{self.slug}/'

class Post(models.Model):
    title = models.CharField(max_length=100)
    team_name = models.CharField(max_length=30, null=False)
    team_member = models.TextField(max_length=100, null=False)
    content = models.TextField()
    img = models.ImageField(blank=True, null=True, upload_to='cheer_photo/%y/%m/%d/')
    file = models.FileField(blank=True, null=True, upload_to='cheer_file/%y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    # user = models.ForeignKey(Account,on_delete=models.CASCADE)
    caption = models.TextField(null=True, blank=True)
    Tag = models.ManyToManyField(Tag,blank=True)
    

    scrap = models.ManyToManyField(User, blank=True, related_name='scrap_name')
    count = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.title

    def extract_tag_list(self):
        tag_list = []
        for tag_name in re.findall(r'#([a-zA-Z\dㄱ-힣]+)', self.caption):
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)
        return tag_list


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user}::{self.content}'

    #추가함
    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment--{self.pk}'

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50, unique=True)
    slug = models.SlugField(max_length=200,unique=True,allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/mainapp/category/{self.slug}/'

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    Tag = models.IntegerField(2)
    category = models.ForeignKey(Category, null=True, blank = True, on_delete=models.SET_NULL)
    img = models.ImageField(blank=True, null=True, upload_to='cheer_photo/%y/%m/%d/')
    file = models.FileField(blank=True, null=True, upload_to='cheer_file/%y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(Account,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Meta:
    verbose_name_plural = 'Categories'
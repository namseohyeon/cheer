from django.contrib import admin
<<<<<<< HEAD
from .models import Post, Comment,Category
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
=======
from .models import Post, Category
# Register your models here.
admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)
>>>>>>> 7a05a9813d913561c53a0afdd97cda6985cffd20

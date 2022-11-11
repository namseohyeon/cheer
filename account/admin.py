from django.contrib import admin
from account.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm
# Register your models here.

class AccountAdmin(UserAdmin):
    add_form = UserCreationForm

    list_display = ('email', 'name', 'studentNo')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'studentNo')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'studentNo', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, AccountAdmin)
admin.site.unregister(Group)
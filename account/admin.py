from django.contrib import admin
from account.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm
# Register your models here.

class AccountAdmin(UserAdmin):
    add_form = UserCreationForm

    list_display = ('email', 'name', 'studentNo', 'is_admin', 'vote')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_admin')}),
        ('Personal info', {'fields': ('name', 'studentNo', 'vote')}),
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

    actions = ['make_vote_null']

    def make_vote_null(self, request, queryset):
        updated_count = queryset.update(vote='')
        self.message_user(request, '{}건을 vote=null 상태로 변경'.format(updated_count))
    make_vote_null.short_description = '지정 계정의 투표 내역을 NULL로 변경'
admin.site.register(User, AccountAdmin)
admin.site.unregister(Group)
from collections.abc import Callable, Sequence
from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpRequest

from .forms import *
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = User

    list_display = ('username', 'email', 'is_active','is_staff', 'is_superuser', 'last_login')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'last_login')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'first_name', 'last_name', 'profile_pic', 'website', 'bio', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    readonly_fields = ('date_joined', 'last_login')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )

    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('last_login',)

class UserFollowingAdmin(admin.ModelAdmin):
    add_form = UserFollowingCreationForm
    form = UserFollowingChangeForm
    
    model = UserFollowing

    list_display = ('follower', 'followed', 'followed_at')
    list_filter = ('followed_at',)

    readonly_fields = ('follower', 'followed_at')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('followed',)}
         ),
    )

    search_fields = ('follower',)
    ordering = ('-followed_at',)
    
    def get_fieldsets(self, request, obj):
        if not obj:
            return (
                (None, {'fields': ('followed',)}),
            )
        
        return (
            (None, {'fields': ('followed', 'follower')}),
            ('Date', {'fields': ('followed_at',)})
        )
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.follower = request.user
        
        return super().save_model(request, obj, form, change)

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserFollowing, UserFollowingAdmin)
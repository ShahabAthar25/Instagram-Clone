from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = User

    list_display = ('username', 'email', 'is_active','is_staff', 'is_superuser', 'last_login')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'last_login')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'first_name', 'last_name', 'website', 'bio', 'password')}),
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

    fieldsets = (
        (None, {'fields': ('follower', 'followed')}),
        ('Dates', {'fields': ('followed_at',)})
    )
    readonly_fields = ('followed_at',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('follower', 'followed')}
         ),
    )

    search_fields = ('follower',)
    ordering = ('followed_at',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserFollowing, UserFollowingAdmin)
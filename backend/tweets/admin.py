from typing import Any
from django.contrib import admin

from .forms import *
from .models import *

class TweetAdmin(admin.ModelAdmin):
    add_form = TweetCeationChangeForm
    form = TweetCeationChangeForm
    
    model = Tweet

    list_display = ('owner', 'content', 'views', 'created_at')
    list_filter = ('created_at',)

    fieldsets = (
        (None, {'fields': ('content', 'quote_tweet')}),
        ('Statistics', {'fields': ('views',)}),
        ('Dates', {'fields': ('created_at',)})
    )
    readonly_fields = ('views', 'created_at')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('content', 'quote_tweet')}
         ),
    )

    search_fields = ('owner', 'content')
    ordering = ('-created_at',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.owner = request.user

        return super().save_model(request, obj, form, change)

admin.site.register(Tweet, TweetAdmin)